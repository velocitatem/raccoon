const { OpenAILLM, SuppresServer, DataGenerator, AlephAlphaLLM } = require('/home/velocitatem/Documents/Projects/suppress/suppress/suppress.js');
const config = require('../config.json');

const openAILLM = new OpenAILLM(config.key);
prompt = `
Wikipedia is a free, online encyclopedia that operates under an open-source management style. It is the largest and most-read reference work in history, with over 6 million articles in the English-language version alone. It is hosted by the Wikimedia Foundation, a non-profit organization funded mainly through donations. Wikipedia is written and maintained by a community of volunteers, known as Wikipedians, through open collaboration and using a wiki-based editing system called MediaWiki. Its unique structure allows anyone to edit and create pages, which has been praised for enabling the democratization of knowledge. Wikipedia has been widely used as a corpus for linguistic research in computational linguistics, information retrieval, and natural language processing. It commonly serves as a target knowledge base for the entity linking problem and to the related problem of word-sense disambiguation. Anyone can sign up for a Wikipedia account and create a page about anything, even themselves. Wikipedia is available in over 329 languages, covering the most popular worldwide languages.
Wikipedia can help with understanding the world by providing information on many different topics.
Wikipedia is enabled by wiki software, otherwise known as wiki engines, which allow content to be written using a simplified markup language and sometimes edited with the help of a rich-text editor. There are dozens of different wiki engines in use, both standalone and part of other software, such as bug tracking systems. Some wiki engines are free and open-source, whereas others are proprietary. Some permit control over different functions, such as editing rights, while others may permit access without enforcing access control. Other rules may be imposed to organize content.
`



const server = new SuppresServer();
class QA {
    constructor() {
        this.ai = new AlephAlphaLLM({apiKey:config.alephKey,
                            task:"qa",
                            model:"luminous-extended"});
        this.context = prompt;
    }
    async generate(question) {
        console.log(question);
        let ctx = {question:`How can Wikipedia help with: ${question.issue}`, context:this.context}
        console.log(ctx);
        let res = await this.ai.generate(ctx);
        return res;
    }
}

server.createEndpoint("/help", "GET", new QA());

// host the index.html file in the current directory
server.app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});


server.start(3000);
