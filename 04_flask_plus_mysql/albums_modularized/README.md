# Step by Step
---
## Get All Albums Request
1. Client makes an http get request to `/albums`
2. The @classmethod `Album.find_all()` executes
3. The SQL query in `Album.find_all()` runs when we call `query_db(query)`
4. It returns a list of dictionaries (results)
5. We turn that list of dictionaries into a list of Album objects
6. By for looping over results and instantiating an Album object per dictionary
7. Add each Album object to the albums list.
8. Return the albums list. It now contains Album objects
9. In the controller, we catch that returned list in a variable called albums. `albums = Album.find_all()`
10. Send it in a template variable for use in HTML. `albums = albums`

## Get One Album by ID Request
1. Client makes an http get request to `/albums/<int:album_id>`.
2. In the controller method, we create a data dictionary with one key value pair `'id': album_id`.
3. The @classmethod `Album.find_one_by_id(data)` executes with our data dictionary passed in as an argument.
4. The SQL query in find_one_by_id runs when we call `query_db(query, data)`. We fill in the `%(id)s` placeholder with the corresponding key-value pair in the data dictionary.
5. It returns a list containing one dictionary at index 0 in the results list.
6. We turn that dictionary into an Album object and store it in a variable called album. `album = Album(results[0])`
7. Return the Album object `return album`.
8. In the controller, we catch that returned object in a variable called album. `album = Album.find_one_by_id(data)`
9. Send it in a template variable for use in HTML. `album = album`