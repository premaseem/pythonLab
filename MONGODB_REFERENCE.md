# MONGODB QUIRES AND CONCEPTS 


## Data Modelling
Data in MongoDB has a flexible schema.documents in the same collection. They do not need to have the same set of fields or structure Common fields in a collection’s documents may hold different types of data.

### Data Model Design
MongoDB provides two types of data models:  
Embedded data model and Normalized data model. 
Based on the requirement, you can use either of the models while preparing your document.

Embedded Data Model
In this model, you can have (embed) all the related data in a single document, it is also known as de-normalized data model.

For example, assume we are getting the details of employees in three different documents namely, Personal_details, Contact and, Address, you can embed all the three documents in a single one


## Aggreagation 

Aggregations operations process data records and return computed results.
It performs a variety of operations on the grouped data to return a single result. In SQL count(*) and with group by is an equivalent of MongoDB aggregation.

>db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)

db.books.aggregate([
{ $group : { _id: "field" , "projectedName" : {$sum : 1} }
}
])

