const express = require("express");
const { Pool } = require("pg");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "postgres",
  password: "suvi0325",
  port: 5432,
});

app.get("/", (req, res) => {
  res.send("S4learnHub Backend Running 🚀");
});

app.post("/register", async (req, res) => {
  const { username, email, password } = req.body;

  try {
    await pool.query(
      "INSERT INTO users (username, email, password) VALUES ($1,$2,$3)",
      [username, email, password]
    );
    res.json({ message: "User Registered ✅" });
  } catch (err) {
    console.log(err);
    res.status(500).send("Error");
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
