# Plan

This is the plan for the project.
Anything and everything should be planned here.

## Table of contents
1. [Websocket format](#ws)
2. [Api structure](#api)
3. [User interface](#ui)
4. [Testing and debugging](#testing)

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
TODO

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
  * Text data
  * Malformed JSON data