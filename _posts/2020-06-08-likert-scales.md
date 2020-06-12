---
title: "Rating (Likert) scales"
categories:
  - Case-study
tags:
  - survey
  - examples
sidebar:
  nav: "docs"
---

<style>
.color-label {
  font-size: x-large !important;
  color: #425563;
}

.color-hex-codes {
  font-size: small !important;
  color: #19267C;
}

.chart-title {
    font-family: Roboto,sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 21px;
    color: #000;
}
</style>

# TODO

- Divergent stacked bar chart in Excel
- a note on using alluma green


There are many different ways to visualize survey data and just like with most tasks in data visualization, there is not one right answer. 

In this guide we will go through a few ways to visualize what is known as _likert scale data_ and what each of them highlights or downplays. T

# What the data looks like

<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-pO9L9" src="https://datawrapper.dwcdn.net/pO9L9/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="267"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

# Color schemes

Diverging color schemes to illustrate both extremes of the spectrum are opposites.

Keep in mind colors have connotations: when you see something go from red to blue most people assume it's going from bad to good. Having the "positive" end of the spectrum using Red and the negative using Blue could be misleading. 

Be conscious that **red** is usually seen as a negative, if you don't want that connotation for your chart use another color like yellow

Try using other colors like our yellow to blue scale instead.

<div id="observablehq-30f8f623">
  <div class="observablehq-likert_rdbu"></div>
  <br>
  <div class="observablehq-likert_yebu"></div>
</div>
<small class="text-muted">Click on the color squares to copy the list of hex codes.</small>


# Examples
## Bar charts

emphasizes the largest share of the total (i.e. "the biggest share of those who make $150,000+ a year are those who care 'some' about the use of the word 'data' as a plural or singular noun"). This is not particularly useful, you're highlighting one of the two possible positive answers. It is not clear if the sum of both "Some" and "A lot" is larger than the sum of "Not at all" and "Not much". 
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-hP6dc" src="https://datawrapper.dwcdn.net/hP6dc/3/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-GeJ3z" src="https://datawrapper.dwcdn.net/GeJ3z/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

This type of chart could be useful if there is one category that is clearly much larger than the other three for most groups. 

<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-HdKTe" src="https://datawrapper.dwcdn.net/HdKTe/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-EUNIz" src="https://datawrapper.dwcdn.net/EUNIz/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

This logic is true for [horizontal bar charts too](#horizontal-bar-charts)

## Pie charts
Part of whole. Mostly good when it's clean easy-to-visualize slices (10%, 25%, 33%, etc)
<!-- Pie charts -->
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-Hju43" src="https://datawrapper.dwcdn.net/Hju43/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="299"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-CA87U" src="https://datawrapper.dwcdn.net/CA87U/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="299"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

## Diverging stacked bars

<strong><span class="chart-title">How much, if at all, do you care about the debate over the use of the word "data" as a singular or plural noun?</span></strong>
![stacked-bars-red-to-blue.png]({{ 'assets/images/diverging-stacked-bars-rdbu.png' | relative_url }})

<strong><span class="chart-title">How much, if at all, do you care about the debate over the use of the word "data" as a singular or plural noun?</span></strong>
![stacked-bars-yellow-to-blue.png]({{ 'assets/images/diverging-stacked-bars-yebu.png' | relative_url }})

Here is an excel workbook to get you started with diverging stacked bar charts: [link to workbook]({{ 'assets/resources/diverging-bar-charts.xlsx' | relative_url }})

## Stacked bar charts
<!-- Stacked bar charts -->
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Stacked Bars" id="datawrapper-chart-l8nJA" src="https://datawrapper.dwcdn.net/l8nJA/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="291"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Stacked Bars" id="datawrapper-chart-KTlJ2" src="https://datawrapper.dwcdn.net/KTlJ2/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="291"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>



# Further reading

- [Wikipedia: Likert scale - Wikipedia](https://en.wikipedia.org/wiki/Likert_scale)
- [Seven different ways to display Likert scale data - Nightingale](https://medium.com/nightingale/seven-different-ways-to-display-likert-scale-data-d0c1c9a9ad59?source=friends_link&sk=60cb93604b71ecc8820cc785ed1afd1a)
- [The case against diverging bar charts - Datawrapper](https://blog.datawrapper.de/divergingbars/)


<!-- Observable HQ -->
<script type="module">
  import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
  import define from "https://api.observablehq.com/@chekos/alluma-data-visualization-style-guide.js?v=3";
  (new Runtime).module(define, name => {
    if (name === "likert_rdbu") return Inspector.into("#observablehq-30f8f623 .observablehq-likert_rdbu")();
    if (name === "likert_yebu") return Inspector.into("#observablehq-30f8f623 .observablehq-likert_yebu")();
  });
</script>


## Horizontal bar charts
See [bar charts](#bar-charts) section.
<!-- Horizontal bar charts -->
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Grouped Bars" id="datawrapper-chart-5wcjq" src="https://datawrapper.dwcdn.net/5wcjq/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="706"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Grouped Bars" id="datawrapper-chart-iuoJR" src="https://datawrapper.dwcdn.net/iuoJR/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="706"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
