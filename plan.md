# Plan

This is the plan for the project.
Anything and everything should be planned here.

## Table of contents
1. [Division of work](#work)
2. [Websocket format](#ws)
3. [Api structure](#api)
4. [User interface](#ui)
5. [Testing and debugging](#testing)
6. [Database structure](#db)
7. [Kitchen view structure](#kvs)

### Division of work <a name="work"></a>
We will divide the work as follows:
* Mikko: Frontend and documentation.
* Leo: BurgerOrderer and documentation.
* Filip: KitchenView, documentation and docker.

We decided this in the beginning of the project but forgot to write it down.

### Websocket format <a name="ws"></a>
This is how the websocket messages will be formatted. This will only make sense if you also read [Api structure](#api). In the title web sockets will be denoted by the start `WebSocket`. It will then have the name of the operation e.g `newOrder`. This title is not a URL like the the rest of the API but rather a part of the message. We therefore have a custom `Packet` which defines the `name` where the name of the operation is stored.. Packets will look like the following:
```json
{
  "name": "string",
  "data": {}
}
```

Heres an example packet from `newOrder`:
```json
{
  "name": "newOrder",
  "data": {
    "burgerName": "cheeseBurger",
    "specials": [
      "+pickels",
      "-tomatoes"
    ]
  }
}
```
In python it might look something like this:
```python
class Packet:
  def __init__(self, name: str, data: str):
    self.name = name
    self.data = data
```

### Api structure <a name="api"></a>

#### Everything customer

<details>
 <summary><code>GET</code> <code><b>/</b></code> <code>(gets the main order page for the customer)</code></summary>

##### Parameters

> None

##### Responses

> | http code | content-type               | response     |
> |-----------|----------------------------|--------------|
> | `200`     | `text/plain;charset=UTF-8` | `index.html` |

</details>

<details>
 <summary><code>GET</code> <code><b>/api/getBurgers</b></code> <code>(gets all burgers)</code></summary>

##### Parameters

> None

##### Responses

> | http code | content-type       | response          |
> |-----------|--------------------|-------------------|
> | `200`     | `application/json` | `{"burgers": []}` |

</details>

<details>
 <summary><code>GET</code> <code><b>/api/getSpecial{burgerName}</b></code> <code>(gets all special order options for a burger)</code></summary>

##### Parameters

> None

##### Responses

> | http code | content-type       | response           |
> |-----------|--------------------|--------------------|
> | `200`     | `application/json` | `{"specials": []}` |
> | `404`     | `application/json` | `None`             |

</details>


<details>
 <summary><code>POST</code> <code><b>/api/sendOrder</b></code> <code>(sends the customers order to the server)</code></summary>

##### Parameters

> | name  | type     | data type     | description                        | Example                                             |
> |-------|----------|---------------|------------------------------------|-----------------------------------------------------|
> | Order | required | object (JSON) | The customers order in JSON format | `{"order": {"burgerName": "string", specials: []}}` |

##### Responses

> | http code | content-type       | response           |
> |-----------|--------------------|--------------------|
> | `200`     | `application/json` | `{"specials": []}` |
> | `404`     | `application/json` | `None`             |


</details>

#### Everything kitchen

<details>
 <summary><code>WebSocket</code> <code><b>newOrder</b></code> <code>(creates a new order for the kitchen)</code></summary>

##### Received Message (Server -> Client)

> | name  | type     | data type        | description                                   | Example                                |
> |-------|----------|------------------|-----------------------------------------------|----------------------------------------|
> | order | required | application/json | The order that's gonna be made by the kitchen | `{"burger": "string", "specials": []}` |

</details>

### User interface <a name="ui"></a>
You can read it [here](ui-plan.md)

### Testing and debugging <a name="testing"></a>
The testing will be done with the pytest library. It is a popular choice for unit testing in python. It also has built in functionality to work with the flask library. Which we use for out web server(s).

#### Things to test:

Kitchen_view:
---
There is only one endpoint inside of kitchen_view which is the <code><b>/newOrder</b></code> endpoint. Inside it we will test the following:
* A successful order.
* No data.
* Broken burger entry.
* Malformed burger data.
* Empty burger data.
* Broken special entry.
* Malformed special entry.
* Malformed special data.
  
This is a wide range of tests which tests multiple failure points. We would also like to point out that we did think about limiting the size of requests but deemed it unnecessary since it can only be called from inside the local network.

Burger_orderer:
---
There is quite a few endpoints on burger_orderer and we shall breakdown every plan for every endpoint:

* <code>GET</code> <code><b>/api/getBurgers</b></code>
  * A get request to see if the endpoint works and check if a default burger is there.
* <code>GET</code> <code><b>/api/getSpecials</b></code>
  * Check if specials exists for default burger.
  * No burger provided.
  * No burger name provided.
  * Non existent burger name.
* <code>POST</code> <code><b>/api/newOrder</b></code>
  * Valid order
  * No JSON data
  * Malformed JSON data
  

#### Debugging
For debugging the two flask servers we use the free version of Postman. This will allow us to probe and test every api endpoint with any and all data. For general debugging inside of python we use breakpoints and debugging statements such as <code>print()</code>.

To debug the MongoDB server we will use a docker container from docker hub called Mongo-Express. It provides a web interface for the MongoDB instance so we can check if for example data is getting inserted correctly. This can be done in python as well, but comes with some limitations such as having to run the program every time.

### Database structure <a name="db"></a>
The database will have a single collection as it is called in MongoDB. A collection contains documents and documents contain data. We will have a collection of burgers. The documents will contain information of the burgers on the menu. Such as name, price and special customization items. A document looks like this:
```json
{
    _id: ObjectId('670eb591b855155b1befbd18'), // a unique id for each document. this is a mongodb feature.
    name: 'Cheeseburger',
    price: '2000kr',
    specials: [
        'Add pickles',
        'Add tomatoes',
        'Remove cheese',
        'Remove ketchup',
        'Remove onions'
    ]
}
```

### Kitchen view structure <a name="kvs"></a>
The kitchen view will print to std output. It will print in the following format:
```
New order:
------------------------------
Type of burger:    Cheeseburger
Special requests:  Add pickles, remove cheese
------------------------------
```