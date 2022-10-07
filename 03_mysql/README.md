# MySQL
---
## What is MySQL?

A relational database management system. (RDBMS). MySQL is by far the most widely used RDBMS.

Downloads today:
- MySQL Server
- MySQL Workbench (GUI)

Hierarchy of MySQL
- Schemas (databases) - you'll probably have one schema or database per project.
- Inside the schema, you'll have one or more tables.
- The tables will have columns.
- Each row in the table corresponds to one record in the table.

ERD First Method
Entity Relationship Diagram

## Naming Conventions
- Table names are lowercase plural nouns
- Primary key - 'id'. Also auto-incremented.
- Add created_at and updated_at.
- created_at is default CURRENT_TIMESTAMP
- updated_at is default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
- All columns that do not have a default value should have the NOT NULL constraint (NN checkbox).