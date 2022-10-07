# RESTFUL ROUTING
---

| FUNCTION NAME    | ROUTE                           | METHOD | PURPOSE                        | TEMPLATE NAME   |
|------------------|---------------------------------|--------|--------------------------------|-----------------|
| `all_things()`   | `/things`                       | GET    | display all things             | all_things.html |
| `new_thing()`    | `/things/new`                   | GET    | display form to create a thing | new_thing.html  |
| `create_thing()` | `/things`                       | POST   | process form to create a thing | N/A             |
| `one_thing()`    | `/things/<int:thing_id>`        | GET    | display one thing              | one_thing.html  |
| `edit_thing()`   | `/things/<int:thing_id>/edit`   | GET    | display form to edit a thing   | edit_thing.html |
| `update_thing()` | `/things/<int:thing_id>/update` | POST   | process form to update a thing | N/A             |
| `delete_thing()` | `/things/<int:thing_id>/delete` | GET    | delete one thing               | N/A             |