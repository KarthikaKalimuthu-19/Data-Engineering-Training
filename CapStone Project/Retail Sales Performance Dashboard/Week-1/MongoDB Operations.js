// Store promotional campaign feedback in MongoDB

use retail_campaigns;
switched to db retail_campaigns

db.campaign_feedback.insertOne({
  productID: 1,
  storeID: 1,
  campaignName: "Sale-2k25",
  startDate: new Date("2025-06-01"),
  endDate: new Date("2025-06-15"),
  feedback: [
    {
      customerID: 1,
      rating: 4,
      comment: "Nice",
      timestamp: new Date("2025-06-02")
    },
    {
      customerID: 2,
      rating: 5,
      comment: "Good offers",
      timestamp: new Date("2025-06-03")
    }
  ]
});
{
  acknowledged: true,
  insertedId: ObjectId('6880fdbe9d2a437bd0d12a34')
}

// Add indexes to search by product and region

db.campaign_feedback.createIndex({ productID: 1 });

db.campaign_feedback.createIndex({ storeID: 1 });

db.campaign_feedback.createIndex({ campaignName: 1 });