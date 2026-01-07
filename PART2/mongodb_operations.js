/* TASK 2.2 - MONGODB IMPLEMENTATION*/

/*SELECT DATABASE*/

USE fleximart_nosql;


/*OPERATION 1: LOAD DATA

Data is already imported using MongoDB Compass
or mongoimport command as shown below.

mongoimport --db fleximart_nosql --collection products \
--file products_catalog.json --jsonArray

*/


/*OPERATION 2*/

db.products.find(
  {
    category: "Electronics",
    price: { $lt: 50000 }
  },
  {
    _id: 0,
    name: 1,
    price: 1,
    stock: 1
  }
);


/*OPERATION 3*/

db.products.aggregate([
  {
    $unwind: "$reviews"
  },
  {
    $group: {
      _id: "$name",
      average_rating: { $avg: "$reviews.rating" }
    }
  },
  {
    $match: {
      average_rating: { $gte: 4.0 }
    }
  }
]);


/*OPERATION 4*/

db.products.updateOne(
  { product_id: "ELEC001" },
  {
    $push: {
      reviews: {
        user_id: "U999",
        username: "StudentUser",
        rating: 4,
        comment: "Good value for money",
        date: new Date()
      }
    }
  }
);


/*OPERATION 5*/

db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avg_price: { $avg: "$price" },
      product_count: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      category: "$_id",
      avg_price: 1,
      product_count: 1
    }
  },
  {
    $sort: { avg_price: -1 }
  }
]);
