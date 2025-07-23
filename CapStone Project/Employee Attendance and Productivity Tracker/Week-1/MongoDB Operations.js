// Use MongoDB to store unstructured task feedback and notes

use employee_tracker;
switched to db employee_tracker

db.createCollection("taskFeedbacks");
db.createCollection("employeeNotes");

db.taskFeedbacks.insertOne({
  employeeID: 1,
  taskID: 1,
  date: new Date("2024-06-01"),
  feedback: "Good work!"
});
{
  acknowledged: true,
  insertedId: ObjectId('6880f9b0a2888cd94fd7b450')
}

db.employeeNotes.insertOne({
  employeeID: 1,
  department: "AI",
  noteType: "Warning",
  note: "Absent 3 days in last week",
  createdBy: "AI_Engineer_01", 
  timestamp: new Date("2024-06-01")
});
{
  acknowledged: true,
  insertedId: ObjectId('6880f9c6a2888cd94fd7b451')
}

// Create indexes for fast querying by employee_id or department

db.employeeNotes.createIndex({ employeeID: 1 });

db.taskFeedbacks.createIndex({ taskID: 1 });