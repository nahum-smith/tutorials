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
