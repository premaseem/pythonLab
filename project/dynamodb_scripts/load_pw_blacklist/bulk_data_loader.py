#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import boto3
import configparser
import logging.config
import os.path
from botocore.exceptions import ClientError, ParamValidationError
import datetime
total_records_in_file = 0
total_inserted_records = 0
total_failed_records = 0


def increment_error_count():
    global total_failed_records
    total_failed_records += 1


def load_data(input_file, dynamo_table):
    try:
        with open(input_file) as f:
            for line in f:
                global total_records_in_file
                total_records_in_file += 1

                # get prepared item
                item = prepare_item(line)

                if item:
                    insert_data_in_dynamodb(item, dynamo_table)
                else:
                    logging.error("Skipped adding line due to error " + str(line))
                    increment_error_count()
    except Exception as e:
        print(e)


def insert_data_in_dynamodb(item, table):
    try:
        logging.debug("inserting " + str(item))
        table.put_item(Item=item)
        global total_inserted_records
        total_inserted_records += 1
        if total_inserted_records % 100 == 0:
            print(".",end="")

    except ParamValidationError as e:
        increment_error_count()
        logging.error("Parameter validation error: %s" % e)

    except ClientError as e:
        increment_error_count()
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            logging.error("Password already exists in Database")
        else:
            logging.error(e.response['ResponseMetadata']['RequestId'])
            logging.error(e.response['Error']['Message'])


def prepare_item(line):
    item = None
    try:
        attr_values = line.strip().split(':')
        pass_hash = attr_values[0]
        count = attr_values[1]
        item = {
            'pwd_hash': pass_hash,
            'count': parse_int(count)
        }
    except Exception as e:
        logging.error("Error occurred while parsing " + str(attr_values))
        logging.error(e)
    return item


def parse_int(value):
    try:
        return int(value)
    except ValueError:
        pass
    # in case int cannot be parsed 0 will be returned as count
    return 0



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DynamoDb data loader")
    # parser.add_argument('-f', dest='input_file_path',default="10.million.10.txt",
    parser.add_argument('-f', dest='input_file_path',default="input-10.txt",
                        help='please provide path of input file to load data')
    parser.add_argument('-c', dest='config_file_path',
                        default='resources/config.properties',
                        help='please provide path of config.properties file')
    parser.add_argument('-l', dest='log_config_file_path',
                        default='resources/logging.properties',
                        help='please provide path of logging.properties file')

    config = configparser.ConfigParser()
    inputs = parser.parse_args()

    if inputs.input_file_path is None:
        print("Please use -f to pass input file path")
        quit()

    if not os.path.isfile(inputs.config_file_path) or not os.path.isfile(
            inputs.log_config_file_path):
        print(
            "Please provide valid config file path for arg -c `config.properties` and arg -l 'logging.properties")
        quit()

    try:
        config.read([inputs.config_file_path])
        logging.config.fileConfig(inputs.log_config_file_path)
    except Exception as ex:
        print("invalid path for configuration files")
        logging.error(ex)
        quit()

    endpoint = config['dynamodb']['endpoint_url']
    region = config['dynamodb']['region']
    table_name = config['dynamodb']['table_name']

    dynamodb = boto3.resource('dynamodb', region_name=region,
                              endpoint_url=endpoint)
    table = dynamodb.Table(table_name)
    start_time = datetime.datetime.now()
    load_data(inputs.input_file_path, table)

    end_time = datetime.datetime.now()
    time_to_upload = (end_time - start_time)
    logging.info(
        "***** Consolidated report of data insertion for the input file {}".format(
            inputs.input_file_path))

    logging.info("Number of records {}".format(total_records_in_file))
    logging.info(
        "Number of records inserted {}".format(total_inserted_records))
    logging.info(
        "Number of records failed to insert {}".format(total_failed_records))
    logging.info( "Time Started: {}".format(start_time))
    logging.info( "Time Ended {}".format(end_time))
    logging.info( "Time taken {}".format(time_to_upload))
    os.rename(inputs.input_file_path, inputs.input_file_path + "-done" )

    # logging.info( "Upload rate per second is {}".format(total_inserted_records//time_to_upload))

