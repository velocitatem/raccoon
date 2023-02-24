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

let prompt2 =`Give me a 3 ideas what I should eat for breakfast and clearly start every of them with \"---\" so I can programatically split them. Please consider the following food intolarence: Gluten free. Make sure not to include complex or hard cooking recipes only easy ones that don't require advanced cooking skills. Concatenate the food names in hungarian after the english name inside brackets. The users name is: {param}`

server.createEndpoint(
    "/food/:param",
    "GET",
    new DataGenerator(prompt2, null, llm).set({doFormat: false}));

server.start(3042);
