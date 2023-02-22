const { OpenAILLM, SuppresServer, DataGenerator } = require('ai.suppress.js');
const config = require('./config.json');
const server = new SuppresServer();
const llm = new OpenAILLM(config.key);

const prompt = "{introduction}\nBased on the above introduction, list the following information: Name, Age and Location:";


server.createEndpoint(
    "/new/person/:introduction",
    "GET",
    new DataGenerator(prompt, null, llm).set({doFormat: false}));

let prompt1 =
    `Predict the capital of a country.

Country: {country}
Capital:`

server.createEndpoint(
    "/capital/:country",
    "GET",
    new DataGenerator(prompt1, null, llm).set({doFormat: false}));

server.start(3042);
