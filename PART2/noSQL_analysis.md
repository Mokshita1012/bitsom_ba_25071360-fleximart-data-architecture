-- TASK 2.1 - NOSQL JUSTIFICATION REPORT

NoSQL Database Analysis – FlexiMart

Section A: Limitations of RDBMS

Relational databases like MySQL work well for structured and fixed data models, but they face limitations when handling highly diverse product information. In FlexiMart, different product categories have different attributes. For example, laptops require specifications such as RAM, processor, and storage, while shoes require size, color, and material. In an RDBMS, this would require many nullable columns or multiple additional tables, making the schema complex and inefficient.

Another challenge is frequent schema changes. Whenever a new product type is introduced, the relational schema must be altered using ALTER TABLE commands. These changes can cause downtime, increase maintenance effort, and slow down development. Managing evolving schemas becomes difficult as the product catalog grows.

Storing customer reviews is also problematic in relational databases. Reviews require multiple related tables and joins to store ratings, comments, and review dates. This increases query complexity and impacts performance when fetching complete product details along with reviews.



Section B: Benefits of MongoDB

MongoDB addresses these issues using a flexible, schema-less document model. Each product is stored as a document, allowing different products to have different fields. Laptops, shoes, and groceries can store their specific attributes without affecting other documents, making the system highly adaptable.

MongoDB supports embedded documents, which allows customer reviews to be stored directly inside the product document. Ratings, comments, and review dates can be retrieved in a single query, improving performance and simplifying data access.

Additionally, MongoDB supports horizontal scalability through sharding. As FlexiMart’s product catalog and user base grow, data can be distributed across multiple servers, ensuring high availability and better performance for large-scale applications.



Section C: Trade-offs of Using MongoDB

Although MongoDB offers many advantages, it also has some disadvantages compared to relational databases. One limitation is its weaker support for complex transactions that involve multiple documents. While MongoDB supports multi-document transactions, they are usually harder to implement and may perform slower than transactions in relational databases such as MySQL. 

Another drawback is that MongoDB does not strictly enforce schemas or relational constraints like foreign keys. This means data consistency must be managed at the application level. For systems that require strong data integrity, strict schemas, and complex relational queries, MySQL can still be a more reliable and suitable choice.