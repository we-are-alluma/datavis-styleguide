// Load the Observable runtime and inspector.
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";

// Your notebook, compiled as an ES module.
import notebook from "https://api.observablehq.com/d/8a46bccde7c8640b.tgz?v=3";

// Load the notebook, observing its cells with a default Inspector
// that simply renders the value of each cell into the provided DOM node.
new Runtime().module(notebook, Inspector.into(document.body));