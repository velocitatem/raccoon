const express = require('express');
const app = express();
let port = 8000;

// read the port from config.json
const config = require('./config.json');
port = config.port;

// create an http server with some endpoints GET
// GET /validate -> return "I thought I would sail about a little and see the watery part of the world"

app.get('/validate', (req, res) => {
  res.send('I thought I would sail about a little and see the watery part of the world');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});
