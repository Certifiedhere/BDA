# BDA

# Practi 2

- insert One & Many

```json
use msccs
```

```json

db.kc.insert({roll_no:1,name:"Nihal",sem:5,sgpa:8.87})
```

```json
db.kc.insertMany({roll_no:2,name:"Rizwan",sem:5,sgpa:8.99},{roll_no:3,name:"Aisha",sem:5,sgpa:9.56},{roll_no:4,name:"Talib",sem:5,sgpa:5.44},{roll_no:5,name:"Safiya",sem:5,sgpa:10.00})
```
```json
db.kc.find()
```

```json
db.kc.find().pretty()
```
```json
db.kc.find().limit(2)
```

```json
db.kc.find().skip(3)
```

- “AND” Condition ⇒

```json
db.kc.fi nd({$and:[{sem:{$eq:5}},{sgpa:{$eq:3.5}}]})
```

```json
db.kc.find({roll_no:4})
```

- “OR” Condition ⇒

```json
db.kc.find({$or:[{sem:{$eq:5}},{roll_no:{$eq:3}}]})
```

- Count ⇒

```json
db.kc.find().count()
```

- Sort Ascending Order ⇒

```json
db.kc.find().sort({name:1})
```

- Sort Descending Order ⇒

```json
db.kc.find().sort({name:-1})
```

- Update Operation ⇒

```json
db.kc.update({roll_no:1},{$set:{name:shebel}})
```

- Update Many ⇒

```json
db.kc.updateMany({sem:{$gt:4}},{$set:{sgpa:9.5}})
```

- Delete Operation ⇒

```json
db.kc.deleteOne({roll_no:3})
```

- Adding a new record, containing a new attribute named hobbies which contains values in an array.

```json
db.kc.insert({roll_no:6,name:"Siddiqui",sem:5,sgpa:8.87,hobbies:["football","cricket"]});
```

# practi 3

insert One

```json
use Blog

db.blog.insert({id:1,title:"New Post",desc:"This is a new post",url:"blog/new-post",postby:"Nihal Siddiqui",likes:200,comments:[{user:"Nihal",message:"Nice Post",added_on:"12-12-2022",likes:100}],tags:[{user:"Rizwan",message:"First Comment",added_on:"02-09-2023",likes:120}]})

```

- insert Many

```json

db.blog.insertMany([{id:2,title:"Post 2",desc:"This is post 2",url:"blog/new-post-2",postby:"Rizwan Ansari",likes:250,comments:[{user:"Nihal",message:"Hey",added_on:"06-09-2023",likes:150}],tags:[{user:"Shebel",message:"second post First Comment",added_on:"10-04-2023",likes:100},{user:"Mohsin",added_on:"13-11-2023",likes:0}]},{id:3,title:"Post 3",desc:"This is 3 post",url:"blog/post-4",postby:"Owner",likes:0,comments:[{user:"Aisha",message:"Heyyyy",added_on:"10-11-2023"}],tags:[{user:"Safiya",added_on:"12-12-2023"}]}])

```

- Post having likes greater than or equal to 150

```json
db.blog.find({"likes":{$gte:150}}).pretty()

```

- Comments having likes greater than equal to 150

```json
db.blog.find({"comments.likes":{$gte:150}}).pretty()
```

- Find post having id 1 or 3

```json
db.blog.find({$or:[{id:1},{id:3}]}).pretty()
```

- Posts not having likes greater than 100 (not Operator)

```json
db.blog.find({likes:{$not:{$gt:100}}}).pretty()
```

- Posts not having ids: 1 and 3 (Nor Operator)

```json
db.blog.find({$nor:[{id:1},{id:3}]}).pretty()

```

- Find posts having titles ‘New Post’ and ‘Post 3’ using In Operator

```json
db.blog.find({title:{$in:["New Post","Post 3"]}}).pretty()
```

- Find posts not having titles ‘New Post’ and ‘Post 3’ using In Operator Not and In Operator

```json
db.blog.find({title:{$not:{$in:["New Post","Post 3"]}}}).pretty()
```

- And and ne (not equal to) operator

```json
db.blog.find({$and:[{likes:{$ne:50}},{"comments.likes":{$ne:10}}]}).pretty()
```

- all operator

```json
db.blog.find({postby:{$all:["Sam","Ben"]}}).count()
```

- regex

```json
db.blog.find({"title":{$regex:/2$/}}).pretty()
```

- Posts posted by Name Starting with S and ending with i.

```json
db.blog.find({postby:{$regex:/^N.*i$/}}).pretty()
```

# pract 4

## Create a mongodb schema with name inventory and contains the following attributes.

1. Item name
2. Quantity
3. Size (height, width and unit of measure)
4. Quality (having grade from A – E)
5. Instock (warehouse [Eg: w1, w2], quantity)

- Insert queries:

```json
insert One

db.inventory.insert({iname:"Ball", quant:30, size:{height:2,width:2,unit:"cm"}, qual:"D",instock:[{whouse:"W4",quantity:20},{whouse:"W2",quantity:10}]});

db.inventory.insert({iname:"Airbrush", quant:12, size:{height:12,width:12,unit:"cm"}, qual:"A",instock:[{whouse:"W1",quantity:8},{whouse:"W4",quantity:4}]});

```

- insert Many

```json
db.inventory.insertMany([{iname:"Chairs", quant:6, size:{height:0.5,width:0.5,unit:"m"}, qual:"C",instock:[{whouse:"W3",quantity:3},{whouse:"W7",quantity:2},{whouse: "W10",quantity:1}]} , {iname:"journal", quant:100, size:{height:24,width:16,unit:"cm"}, qual:"B",instock:[{whouse:"W1",quantity:10},{whouse:"W2",quantity:60},{whouse: "W5",quantity:10},{whouse: "W10",quantity:20}]} , {iname:"Erasers ", quant:500, size:{height:40,width:20,unit:"mm"}, qual:"D",instock:[{whouse:"W4",quantity:100},{whouse:"W3",quantity:100},{whouse: "W5",quantity:300}]}]);

db.inventory.insertMany([{iname:"Duster", quant:40, size:{height:0.2,width:0.1,unit:"m"}, qual:"E",instock:[{whouse:"W1",quantity:12},{whouse:"W2",quantity:12},{whouse: "W10",quantity:26}]} , {iname:"Papers", quant:1000, size:{height:24,width:16,unit:"cm"}, qual:"C",instock:[{whouse:"W4",quantity:500},{whouse:"W6",quantity:500}]} , {iname:"Mouse", quant:30, size:{height:10,width:5,unit:"cm"}, qual:"A",instock:[{whouse:"W10",quantity:10},{whouse:"W9",quantity:10},{whouse: "W8",quantity:10}]}]);

db.inventory.insertMany([{iname:"Keyboard", quant:42, size:{height:0.2,width:0.5,unit:"m"}, qual:"A",instock:[{whouse:"W8",quantity:12},{whouse:"W6",quantity:13},{whouse: "W3",quantity:17}]} , {iname:"Stand", quant:350, size:{height:24,width:30,unit:"cm"}, qual:"B",instock:[{whouse:"W4",quantity:250},{whouse:"W6",quantity:100}]}]);

```

- Find all items having quantity less than or equal to 10

```json
db.inventory.find({quant:{$lte:10}});
```

- Find all items having quality as A and display name and quality only

```json
db.inventory.find({qual:"A"},{iname:1,qual:1});
```

- Having instock warehouse as 1 and display names, instock warehouse and instock quantity.

```json
db.inventory.find({"instock.whouse":{$eq:"W1"}},{iname:1,_id:0, "instock.whouse":1})
```

- Having quality as B and E and display their names and quality.

```json
db.inventory.find({$or:[{qual:"B"}, {qual:"E"}]},{iname:1,_id:0, qual:1})

```

- Having instock quantity between 20 and 40 and display names, quantity and instock data.

```json
db.inventory.find({$and:[{"instock.quantity":{$lte:40}}, {"instock.quantity":{$gte:20}}]},{iname:1,_id:0, qual:1, "instock":1})
```

- Find all items starting with S.

```json
db.inventory.find({iname:{$regex:'S'}}, {iname:1, quant:1, _id:0})
```

- Find all inventory item names having in-stock warehouse as w2 and w5 and w7, show name, warehouse number, except id.

```json
db.inventory.find({"instock.whouse":{$in:["W2", "W5", "W7"]}},{iname:1,_id:0, "instock.whouse":1})
```

- Find all inventory item names having instock warehouse not as w2 and w5 and w7, show name, warehouse number, except id.

```json
db.inventory.find({"instock.whouse":{$nin:["W2", "W5", "W7"]}},{iname:1,_id:0, "instock.whouse":1})
```

- Quality as E and quantity greater than equal to 50.

```json
db.inventory.find({$and:[{qual:"E"}, {quant:{$gte:20}}]},{iname:1,_id:0, qual:1, quant:1})
```

- Item names not having instock quantity greater than equal to 50

```json
db.inventory.find({"instock.whouse":{$nin:["W2", "W5", "W7"]}},{iname:1,_id:0, "instock.whouse":1})
```

- Count of inventory having unit of measure as metre

```json
db.inventory.find().limit(3)
```

- Display first 3 documents

```json
db.inventory.find().limit(3)
```

- Aggregation functions: match-> group-> project-> sort-> limit.

- Display the total quantity of all items.

```json

```

Display the average quantity of items present in each document within the collection.

```json
db.inventory.aggregate([{$group:{_id:null, "Sum of quantity":{$sum:"$quant"}}}])
```

Display which item has the lowest quantity within the collection.

```json
db.inventory.aggregate([{$group:{_id:null, "Average of quantity":{$avg:"$quant"}}}])
```

Display which item has the highest quantity within the collection.

```json
db.inventory.aggregate([{$group:{_id:null, "Minimum quantity":{$min:"$quant"}}}])
```

Display all the items having units in cm using the $match stage.

```json
db.inventory.aggregate([{$match:{"size.units":"cm"}}, {$project:{itemname:1, quantity:1}}])

```

- Match items having quantity greater than equal to 40 quantity

```json
db.inventory.aggregate([{$match: {quant: {$gte:40}}}])
```

- Items having Unit of Measure as metre and display item name and size

```json
db.inventory.aggregate([{$match: {"size.unit":"m"}}, {$project: {iname:1,_id:0, "size.unit":1}}])
```

- Display all inventory items using $match in aggregation.

```json
db.inventory.aggregate([{$match: {}}])
```

- Item names not having: Chairs, journal, duster and display its: Name quantity unit

```json
db.inventory.aggregate([{$match: {iname: {$nin: ["Chairs","journal","Duster"]}}}, {$project: {iname:1,_id:0, quant:1, "size.unit":1}}])
```

- Item names not having: Chairs, journal, duster and display its: Name quantity unit

```json
db.inventory.aggregate([{$match: {iname: {$nin: ["Chairs","journal","Duster"]}}}, {$project: {iname:1,_id:0, quant:1, "size.unit":1}}])
```

- Display all items having instock quantity between 50 and 100, display item name, unit of measure and instock details.

```json
db.inventory.aggregate([{$match: {$and:[{"instock.quantity":{$lte:100}}, {"instock.quantity":{$gte:50}}]}}, {$project: {iname:1,_id:0,"size.unit":1,"instock":1}}])
```

- Display all items having quantity greater than equal to 70 sorted by their quantity in descending order and display their iname and quantity

```json
db.inventory.aggregate([{$match: {quant:{$gte:70}}}, {$sort: {quant:-1}}, {$project:{iname:1, quant:1, _id:0}}])
```

- Display all items with name journals

```json
db.inventory.aggregate([{$match: {iname:"journal"}}])
```

# prcti 06

```json
db.inventory.find()
```

- Perform map reduce on the data to display the sum of quantities of each record

```json
var map1=function(){emit(this.iname, this.quant)};
var reducer1=function(iname,quant){return Array.sum(quant);}
```

```json
 db.inventory.mapReduce(map1, reducer1, {out:"newdoc"})
```

- Perform map reduce to display the average quantites of all items

```json
var reducer2=function(iname,quant){return Array.avg(quant);}
```

```json
db.inventory.mapReduce(map1, reducer2, {out:"newdoc2"})
db.newdoc2.find()
```

- Sort the resultant records in descending order

```json
db.newdoc2.find().sort({value:-1})

```

- Perform Map reduce to display the sum of quantities of records which have quality as ‘A’

```json
db.inventory.mapReduce(map1, reducer1, {query:{qual:"A"}, out:"newdoc3"})
```

- DeprecationWarning: Collection.mapReduce() is deprecated. Use an aggregation instead

```json
db.newdoc3.find()
```

- Perform map reduce to display the average quantity of all records which have quality as ’A’. Display only the first 2 records

```json
 db.inventory.mapReduce(map1, reducer2, {query:{qual:"A"}, out:"newdoc3", limit:2});

```

- Create a single index for quantities of items in ascending order

```json
db.inventory.createIndex({quant:1});

```

- Create an index to store the unit of size and item name both in ascending order and give it a name

```json
db.inventory.createIndex({"size.unit":1,iname:1},{name:"Size and Name index
"})

```

- Show all Indexes

```json
db.inventory.getIndexes()

```

- Delete an index

```json
db.inventory.dropIndex({quant:1})
```

```json
 db.inventory.getIndexes()
```
