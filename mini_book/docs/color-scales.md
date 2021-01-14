# Colors

<style src="{{ site.url }}/assets/css/colors-notebook.css"></style>


<div id="observablehq-30f8f623">
  <div class="observablehq-main_colors"></div>
  <div class="observablehq-main_dark"></div>
  <div class="observablehq-main_medium"></div>
  <div class="observablehq-main_light"></div>
  <div class="observablehq-primary"></div>
  <div class="observablehq-secondary"></div>
  <div class="observablehq-secondary_gray"></div>
  <div class="observablehq-shades_alluma_green"></div>
  <div class="observablehq-shades_alluma_slate"></div>
  <div class="observablehq-shades_red"></div>
  <div class="observablehq-shades_gold"></div>
  <div class="observablehq-shades_lightblue"></div>
  <div class="observablehq-shades_indigo"></div>
  <div class="observablehq-likert_rdbu"></div>
  <div class="observablehq-likert_yebu"></div>
</div>

<script type="module">
  import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
  import define from "https://api.observablehq.com/@chekos/alluma-data-visualization-style-guide.js?v=3";
  (new Runtime).module(define, name => {
    if (name === "style") return Inspector.into(".style-observablehq")();
    if (name === "main_colors") return Inspector.into("#observablehq-30f8f623 .observablehq-main_colors")();
    if (name === "main_dark") return Inspector.into("#observablehq-30f8f623 .observablehq-main_dark")();
    if (name === "main_medium") return Inspector.into("#observablehq-30f8f623 .observablehq-main_medium")();
    if (name === "main_light") return Inspector.into("#observablehq-30f8f623 .observablehq-main_light")();
    if (name === "primary") return Inspector.into("#observablehq-30f8f623 .observablehq-primary")();
    if (name === "secondary") return Inspector.into("#observablehq-30f8f623 .observablehq-secondary")();
    if (name === "secondary_gray") return Inspector.into("#observablehq-30f8f623 .observablehq-secondary_gray")();
    if (name === "shades_alluma_green") return Inspector.into("#observablehq-30f8f623 .observablehq-shades_alluma_green")();
    if (name === "shades_alluma_slate") return Inspector.into("#observablehq-30f8f623 .observablehq-shades_alluma_slate")();
    if (name === "shades_red") return Inspector.into("#observablehq-30f8f623 .observablehq-shades_red")();
    if (name === "shades_gold") return Inspector.into("#observablehq-30f8f623 .observablehq-shades_gold")();
    if (name === "shades_lightblue") return Inspector.into("#observablehq-30f8f623 .observablehq-shades_lightblue")();
    if (name === "shades_indigo") return Inspector.into("#observablehq-30f8f623 .observablehq-shades_indigo")();
    if (name === "likert_rdbu") return Inspector.into("#observablehq-30f8f623 .observablehq-likert_rdbu")();
    if (name === "likert_yebu") return Inspector.into("#observablehq-30f8f623 .observablehq-likert_yebu")();
  });
</script>

<div class="style-observablehq"></div>