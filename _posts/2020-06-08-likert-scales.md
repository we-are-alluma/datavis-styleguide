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

We use surveys to measure people's attitudes all the time and one common way to code answers is using a **Rating scale** or **Likert scale**. These are used to allow survey-takers to express how much they agree or disagree with a statement (`strongly disagree - disagree - undecided - agree - strongly agree`). 


There are variations to measure **frequency** (`never - rarely - sometimes - often - always`), importance (`unimportant - slightly important - moderately important - important - very important`), and quality (`very poor - poor - fair - good - excellent`), among others.

These are, what is known as, **categorical** scales - each answer is its own discrete unit, you cannot answer 'somewhere between slightly important and moderately important', you must choose one. These are also **ordinal** scales - the order matters; 'often' is _more_ than 'rarely' and 'slightly important' is _less_ than 'moderately important' in their respective scales. 


Just like with most tasks in data visualization, there are many different ways to visualize this data and there is not one right answer. 

In this guide we will go through a few ways to visualize **rating-scale** survey answers.

# What the data looks like

First, let's think about how the data looks like. This is from [FiveThirtyEight's Oxford comma survey](https://fivethirtyeight.com/features/elitist-superfluous-or-popular-we-polled-americans-on-the-oxford-comma/).

<iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-pO9L9" src="https://datawrapper.dwcdn.net/pO9L9/3/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="267"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>

This is an agreggated table of answers as you might get from the survey service of your choice. 

**💡Note**: If you received the raw data or individual-level answers, you are going to have to aggregate it yourself. This is easy with pivot tables in excel or using any other data analysis software you prefer. For examples using excel, R and python you can visit the [tidy data section](../../reference/tidy-data) of this style guide.
{: .notice--info }

**What can you tell from this table so far?**

1. There are 4 columns/answers - not 5. This means our scale skips the `neutral/undecided` scale point. Is it because people did not answer the question or because no one actually feels indifferent about Oxford commas? (Impossible!)
2. This table shows total counts - not shares. This means we need to do some more data cleaning ourselves! 

What else can you derive from this table?

# Color schemes

Before diving in further, it is useful to think about the colors we will be choosing for our visualization. Looking at our data categories, we know the answers span from one extreme to the other (`Not at all` to `A lot`). These are opposites and that means we need to use what is known as a _diverging_ color scheme. Diverging color schemes are composed of three colors: one for each end and a neutral color. Gray or white is a common choice for the neutral color. Each of the other two colors sit at the end of the scale and we use lighter and lighter shades of those colors as we approach the center (neutral). 

Keep in mind colors have connotations: when you see something go from red to blue most people assume it's going from bad to good. Having the "positive" end of the spectrum using Red and the negative using Blue could be misleading. 

The color **red** also tends to be seen as a negative in Western societies especially when we are dealing with numbers. If you prefer not to use **red**, try using other colors like our yellow to blue scale instead.

<div id="observablehq-30f8f623">
  <div class="observablehq-likert_rdbu"></div>
  <br>
  <div class="observablehq-likert_yebu"></div>
</div>
<small class="text-muted">Click on the color squares to copy the list of hex codes.</small>


# Examples

Let's go over some ways we could visualize this dataset. Remember, there is not a right answer here. Data can be visualized in many ways and each of them emphasizes and downplays certain aspects of your data. What you want to tell with your data is your choice but please remember to be responsible and honest.

## Bar charts

The simplest chart we can create with our data as it is is a bar chart. In this case, these bar charts emphasize the largest share of the total (i.e. "the biggest share of those who make $150,000+ a year are those who care 'some' about the use of the word 'data' as a plural or singular noun"). 

This is not particularly useful, as we are highlighting one of the two possible positive answers ('some' and 'a lot'). It is not clear if the sum of both "Some" and "A lot" is larger than the sum of "Not at all" and "Not much". 

<!-- Tab links -->
<div class="tab">
  <button id="defaultOpen" class="tablinks" onclick="openCity(event, 'bar-chart-1-red')">Red</button>
  <button class="tablinks" onclick="openCity(event, 'bar-chart-1-yellow')">Yellow</button>
</div>

<!-- Tab content -->
<div id="bar-chart-1-red" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-hP6dc" src="https://datawrapper.dwcdn.net/hP6dc/3/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
  </script>
</div>

<div id="bar-chart-1-yellow" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-GeJ3z" src="https://datawrapper.dwcdn.net/GeJ3z/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
  </script>
</div>

This type of chart could be useful if there is one category that is clearly much larger than the other three for most groups. Take a look:
<!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'bar-chart-2-red')">Red</button>
  <button class="tablinks" onclick="openCity(event, 'bar-chart-2-yellow')">Yellow</button>
</div>

<!-- Tab content -->
<div id="bar-chart-2-red" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-HdKTe" src="https://datawrapper.dwcdn.net/HdKTe/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
  </script>
</div>

<div id="bar-chart-2-yellow" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-EUNIz" src="https://datawrapper.dwcdn.net/EUNIz/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="400"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
  </script>
</div>

This logic is true for [horizontal bar charts too](#horizontal-bar-charts).

## Pie charts
Part of whole. Mostly good when it's clean easy-to-visualize slices (10%, 25%, 33%, etc)

<!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'pie-chart-red')">Red</button>
  <button class="tablinks" onclick="openCity(event, 'pie-chart-yellow')">Yellow</button>
</div>

<!-- Tab content -->
<div id="pie-chart-red" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-Hju43" src="https://datawrapper.dwcdn.net/Hju43/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="299"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
</div>

<div id="pie-chart-yellow" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="chart" id="datawrapper-chart-CA87U" src="https://datawrapper.dwcdn.net/CA87U/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="299"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
</div>

## Diverging stacked bars

<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'diverging-stacked-chart-red')">Red</button>
  <button class="tablinks" onclick="openCity(event, 'diverging-stacked-chart-yellow')">Yellow</button>
</div>

<!-- Tab content -->
<div id="diverging-stacked-chart-red" class="tabcontent">
<strong><span class="chart-title">How much, if at all, do you care about the debate over the use of the word "data" as a singular or plural noun?</span></strong>
<img src="{{ 'assets/images/diverging-stacked-bars-rdbu.png' | relative_url }}">
</div>

<div id="diverging-stacked-chart-yellow" class="tabcontent">
<strong><span class="chart-title">How much, if at all, do you care about the debate over the use of the word "data" as a singular or plural noun?</span></strong>
<img src="{{ 'assets/images/diverging-stacked-bars-yebu.png' | relative_url }}">
</div>

Here is an excel workbook to get you started with diverging stacked bar charts: [link to workbook]({{ 'assets/resources/diverging-bar-charts.xlsx' | relative_url }})

## Stacked bar charts

<!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'stacked-bar-chart-red')">Red</button>
  <button class="tablinks" onclick="openCity(event, 'stacked-bar-chart-yellow')">Yellow</button>
</div>

<!-- Tab content -->
<div id="stacked-bar-chart-red" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Stacked Bars" id="datawrapper-chart-l8nJA" src="https://datawrapper.dwcdn.net/l8nJA/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="291"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
</div>

<div id="stacked-bar-chart-yellow" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Stacked Bars" id="datawrapper-chart-KTlJ2" src="https://datawrapper.dwcdn.net/KTlJ2/2/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="291"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
</div>

# Further reading

- [Wikipedia: Likert scale - Wikipedia](https://en.wikipedia.org/wiki/Likert_scale)
- [Seven different ways to display Likert scale data - Nightingale](https://medium.com/nightingale/seven-different-ways-to-display-likert-scale-data-d0c1c9a9ad59?source=friends_link&sk=60cb93604b71ecc8820cc785ed1afd1a)
- [The case against diverging bar charts - Datawrapper](https://blog.datawrapper.de/divergingbars/)
- [Likert scale - Simple Psychology](https://www.simplypsychology.org/likert-scale.html)


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

<!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'horizontal-bar-chart-red')">Red</button>
  <button class="tablinks" onclick="openCity(event, 'horizontal-bar-chart-yellow')">Yellow</button>
</div>

<!-- Tab content -->
<div id="horizontal-bar-chart-red" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Grouped Bars" id="datawrapper-chart-5wcjq" src="https://datawrapper.dwcdn.net/5wcjq/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="706"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
</div>

<div id="horizontal-bar-chart-yellow" class="tabcontent">
  <iframe title="How much, if at all, do you care about the debate over the use of the word &quot;data&quot; as a singular or plural noun?" aria-label="Grouped Bars" id="datawrapper-chart-iuoJR" src="https://datawrapper.dwcdn.net/iuoJR/1/" scrolling="no" frameborder="0" style="width: 0; min-width: 100% !important; border: none;" height="706"></iframe><script type="text/javascript">!function(){"use strict";window.addEventListener("message",(function(a){if(void 0!==a.data["datawrapper-height"])for(var e in a.data["datawrapper-height"]){var t=document.getElementById("datawrapper-chart-"+e)||document.querySelector("iframe[src*='"+e+"']");t&&(t.style.height=a.data["datawrapper-height"][e]+"px")}}))}();
</script>
</div>

{% include custom-js.html %}