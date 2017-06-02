# Week 1 - Introduction and Overview

### Concept and Rationale

1. scale
    hardware changes
      * parallelism
        * cores
        * servers
      * cloud

    scale up -> 'big data' (with low overhead/cost)

2. Development speed - make app development easier and more elegant
3. Complex Data - complex structure, unstructured,      polymorphic)


#### Scale - Out

Classically companies were limited to scaling vertically, because horizontal scaling required network communication between microservers.  

In vertical monolithic systems, its an all or nothing approach.  If a small portion of the system fails, the entire system fails.  

MongoDB attempts to find the drop off point where more features drastically reduces scalability.  Shooting for 80% of features of Classical SQl Dbs with increased scalability and speed.  

**Question:  
When scaling out horizontally (adding more servers to contain your data), what are the problems that arise as you go from, say, 1 commodity server to a few dozen?**  

**Question:
What causes significant problems for SQL when you attempt to scale horizontally (to multiple servers)**

So what does this mean? -> We need a different data model.

MongoDB uses a Document-Orientated Model (mimicking JSON)

JSON typically looks like 'code' (think JS objects) but JSON is language agnostic/independent, and maps nicely to mainstream programming languages.

**Question:
What are some of the advantages of representing our data using a JSON-like format?**

#### JSON (BSON)

**Question:  
How many data types in JSON?**  

6 Data Types:
  * strings
  * numbers
  * booleans
  * null
  * arrays
  * object/documents

##### Types

### Operators

#### Querying
* $gte
* $gt
* $lt
* $lte
* $or
* $not
* $nin
* $in
* $type


#### Updating
* $inc
* $set
* $addToSet


**Reaching into Nested Documents**
{
  x: {
    a:1, b:33
  }
}
where a=1 inside the x document?
use 'dot' notation

`  db.collections.find("x.a":1)  `

#### Where We Are Going

1. Framework
2. Context
3. CRUD Operations
4. Administrative Commands
5. Performance (singular server)
6. Deployment options
  *
