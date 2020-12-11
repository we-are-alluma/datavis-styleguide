# Line Chart

<style src="{{ site.url }}/assets/css/chart-examples.css"></style>

## When to use a line chart

 * To show the trend in one variable, usually over time.
 * To show multiple variables with multiple lines (if they are on the same scale).
 * To show the same variable for multiple observations with multiple lines.

## Style tips

 * The y-axis should always* start at zero.
 * When possible, directly label series. If too close together, use a legend.
 * Avoid individual data markers.
 * Avoid dashed lines.
 * In a single chart, try to keep the maximum number of lines to three or four. More is not always better. Plotting too many lines on the same chart gives a confusing picture and defeats the purpose.
 * Legends should be stretched across the top of the chart and the order should match the order in the chart.
 * Sequential series should be shaded from lightest to darkest for easy comparison.


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

