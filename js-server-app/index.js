import parseText from "./src/textParser.js";
import parseJson from "./src/jsonParser.js";
import parseYaml from "./src/yamlParser.js";
import parseXml from "./src/xmlParser.js";
import parseCsv from "./src/csvParser.js";

console.log("............................................");
console.log("TXT FILE CONTENT:");

const textPerson = parseText();
console.log(textPerson);
console.log(textPerson.greet());


console.log("............................................");
console.log("JSON FILE CONTENT:");

const jsonPerson = parseJson();
console.log(jsonPerson);
console.log(jsonPerson.greet());


console.log("............................................");
console.log("YAML FILE CONTENT:");

const yamlPerson = parseYaml();
console.log(yamlPerson);
console.log(yamlPerson.greet());


console.log("............................................");
console.log("XML FILE CONTENT:");

const xmlPerson = parseXml();
console.log(xmlPerson);
console.log(xmlPerson.greet());


console.log("............................................");
console.log("CSV FILE CONTENT:");

const csvPerson = parseCsv()
console.log(csvPerson);
console.log(csvPerson.greet());

console.log("............................................");