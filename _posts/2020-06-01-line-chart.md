---
title: "Examples: Line Chart"
categories:
  - Example
tags:
  - charts
  - examples
sidebar:
  nav: "docs"
---
<style src="{{ site.url }}/assets/css/chart-examples.css"></style>


<div id="observablehq-51a86210">
  <div class="observablehq-line_chart"></div>
</div>
<script type="module">
  import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
  import define from "https://api.observablehq.com/@chekos/alluma-data-visualization-style-guide-chart-examples.js?v=3";
  (new Runtime).module(define, name => {
    if (name === "line_chart") return Inspector.into("#observablehq-51a86210 .observablehq-line_chart")();
  });
</script>