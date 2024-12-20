---
theme: "dashboard"
title: Omar Marmoush
toc: false
sidebar: false
pager: false
---
<style>

html{

  font-family: "Bahnschrift", sans-serif;
}

h1, h2, h3 {
  font-family: bahnschrift, sans-serif;

}

figure h2, span{
  font-family: bahnschrift, sans-serif;

}

figure h3 {
  font-family: bahnschrift, sans-serif;

}

p{
  font-family: "Bahnschrift", sans-serif;
}

h2 b{
  font-family: "Bahnschrift", sans-serif;
}

footer{
  font-family: "Bahnschrift", sans-serif;
  height:20px;
}

text, .tooltip {
  font-family: sans-serif;
  font-size: 10pt;
}

text, #tool-data {
  font-family: bahnschrift, sans-serif;
  font-size: 20pt;
}

#container {
max-width: initial;
}


.dim {
  fill-opacity: 0.3;
}

.tooltip {
  position: absolute;
  width: auto;
  height: auto;
  padding: 8px;
  background: #ddd;
  pointer-events: none;
  border: 1px solid #eee;
  border-radius: 10px;
}

.custom-theme {
  --background-color: #2192f2e6;
  --color: #43FCD5;
  --color-meta: #f3efef ;
  --pitch-line-color: #E0FFFF;
  --pitch-shade-color: #cccccc;
  padding-left: 5%;
}

g text{

  font-size: 8px;
}

#assisted g[aria-label="x-axis tick label"] text{
opacity: 0.00001;
}

#actions g[aria-label="x-axis tick label"] text{
opacity: 0.00001;
}

#assisted g[aria-label="y-axis tick label"] text{
opacity: 0.00001;
}

#assisted g[aria-label="y-axis tick"]{
opacity: 0.00001;
}




@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

@media only screen and (max-width: 320px), only screen and (min-width: 321px) (max-device-width: 768px) {

  #tool-data {
      max-width: 408px;
  }
  #chart_card {
      max-width: 408px;
  }

  .custom-theme g#pitch{
  --background-color: #2192f2e6;
  --color: #43FCD5;
  --color-meta: #f3efef ;
  --pitch-line-color: #E0FFFF;
  --pitch-shade-color: #cccccc;
  padding-left: 5%;
  -webkit-transform: rotate(-90deg)scale(0.9, 0.9)translate(-105 0);

}


}


}

</style>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script type="text/javascript" src="https://enadol.de/js/d3-soccer/dist/d3-soccer.min.js"></script>
```js
const data = FileAttachment("./data/goals.csv").csv({typed: true});
//view(Inputs.table(data))
```

```js
const goals = data.filter((d) => d.result == "Goal");
//view(goals)
```
```js
//display(await data)
```

# OMAR MARMOUSH ALL SHOTS SEASON 2024/2025
<div id="container" class="grid grid-cols-3">
  <div id="tool-data" class="card grid-colspan-2 custom-theme" style="background-color: rgb(33 146 242 / 90%);"><h3>SHOT DATA</h3><h2>Hover the mouse on the circles to show the data for each shot</h2></div>
<div id="chart_card" class="card">
<script type="text/javascript">
const HEIGHT_HEADER = 90;
const HEIGHT_PITCH = 300;
const HEIGHT_FOOTER = 20;
var h = 300;
var teams = {
  'Eintracht Frankfurt': { color: 'crimson', side: 'home'},
  Opponent: { color: 'gold', side: 'away' }
  };
const data_omar =(async () =>{ fetch('./_file/omarshots.json')
 .then(response => response.json())
 .then(data_omar => {
 console.log(data_omar);
// aquí puedes trabajar con los datos JSON
 const layer = chartCard.select("#above")
    .selectAll(`circle`)
    .data(data_omar)
    .enter()
    .append("circle")
    .attr("cx", (d) => {
      if (d.h_a === "h") {
        return parseFloat(d.X) * 105;
      } else {
        return parseFloat(d.X) * 105;
      }
    })
    .attr("cy", (d) => 68 - parseFloat(d.Y) * 68)
    .attr("stroke", (d) => teams["Eintracht Frankfurt"].color)
    .attr("stroke-width", 0.2)
    .attr("fill", (d) =>
      d.result === "Goal" ? teams["Opponent"].color : "gold"
    )
    .attr("fill-opacity", 0.5)
    .attr("r", (d) => parseFloat(d.xG) * 5)
    .on("mouseover", function(d) {
      var me = d3.select(this);
      layer.insert("text")
        .attr("id", "label")
        .attr("x", me.attr("cx"))
        .attr("y", me.attr("cy"))
        .attr("dy", parseFloat(d.xG) + 14)
        .attr("text-anchor", "middle")
        .text(d.result);
      // show what we interacted with
      d3.select("#tool-data").html("<h3>SHOT DATA</h3></br>" +"Result: " + d.result+"</br> Home Team: "+d.h_team+"</br> Away Team: "+d.a_team+"</br> Player Assisted: "+d.player_assisted+"</br> Minute: "+d.minute);
    })
    .on("mouseout", function(d) {
      var me = d3.select(this);
      layer.insert("text")
        .attr("id", "label")
        .attr("x", me.attr("cx"))
        .attr("y", me.attr("cy"))
        .attr("dy", parseFloat(d.xG) + 14)
        .attr("text-anchor", "middle")
        .text(d.result);
      // show what we interacted with
        d3.select("#tool-data").html("<h3>SHOT DATA</h3><h2>Hover the mouse on the circles to show the data for each shot</h2>")});
   })
   .catch(error => {
     console.error('Error al leer el archivo JSON:', error);
   });})();
const pitch = d3.pitch().height(h)
  .clip([[0,0],[105,68]])
  .goals("line")
  .rotate(true)
  .showDirOfPlay(false) // Show an arrow on the plot to indicate the direction of play
  .shadeMiddleThird(false) // Shade the middle third of the pitch
  .pitchStrokeWidth(0.5);
const chart = d3.create('div');
var chartCard = d3.select("#chart_card")
    .attr("class", "card custom-theme")
    .style("background-color", "rgb(33 146 242 / 90%)");
const svg = chartCard
    .append("svg")
    .attr("width", pitch.width())
    .attr("height", pitch.height());
const defs = svg.append("defs");
  // Cut pitch in half
defs
  .append("clipPath")
  .attr("id", "cut-half")
  .append("rect")
  .attr("x", 0)
  .attr("y", pitch.width() / 3 - 175)
  .attr("width", pitch.height())
  .attr("height", pitch.width() - pitch.width() / 2 + 60);
 svg
    .append("g")
    .attr("clip-path", "url(#cut-half)")
    .attr("width", pitch.width())
    .attr("height", pitch.height())
    .call(pitch);
// chartCard
//     .append("g")
//     .attr("transform", 'translate(0, 90)')
//     .call(pitch);
// var g = d3.select('#pitch')
//   .attr("width", 70)
//   .attr("transform", "translate(-38,0)");
</script>
</div>
</div>

<div class="grid grid-cols-3">
  <div class="card" id="actions">${
    resize((width) => Plot.plot({title: "Omar Marmoush last actions before shots 🐧",
      width,
      grid: true,
      x: {label: "Last Action", tickRotate: -30},
      y: {label: "Amount"},
      color: {legend: true},
      marks: [
        Plot.dot(action, {x: "lastAction", y: "id", r: "id", stroke: "red", fill: "lastAction"}),
        Plot.tip(action, Plot.pointerX({x: "lastAction", y: "id"}))
      ]})
      )
  }</div>
  <div class="card grid-colspan-2">${
    resize((width) => Plot.plot({
      x: {domain: [0,3], interval: 1},
      y: {domain: [1,91], interval: 1},
      title: "Minute shot intensity 🐧",
      subtitle: "Number of shots by Omar Marmoush per match minute (season)",
      width,
      x: {label: "Minute"},
      y: {label: "Shots"},
      color: {legend: true},
      marks: [
        Plot.ruleX(minutes, {x: "minute", y: "id", curve: "monotone-x", stroke: "violet", strokeWidth: 3}),
        Plot.tip(minutes, Plot.pointerX({x: "minute", y: "id"})),
        Plot.dot(minutes, {x: "minute", y: "id", fill: "grey", r: 3}),
        Plot.axisY({interval: 1})
      ]
    }))
  }</div>
</div>

<div class="grid grid-cols-3">
  <div class="card grid-colspan-2" style="grid-auto-rows: 204px;">${
    resize((width) => Plot.plot({
      title: "Omar Marmoush shots outcome 🐧",
      width,
      marginBottom: 50,
      x: {label: ""},
      y: {label: "Shots"},
      color: {legend: true, scheme: "pastel2", label: "Outcome Range"},
      marks: [
        Plot.rectY(result, {x: "result", y: "id", fill: "id", stroke: "skyblue"}),
        Plot.tip(result, Plot.pointerX({x: "result", y: "id"}))
      ]
    }))
  }</div>
    <div class="card" id="assisted">${
    resize((width) => Plot.plot({title: "Omar Marmoush shot partners 🐧",
          subtitle: "Players that assisted shots by Omar Marmoush",
      width,
      marginLeft: 70,
      marginBottom: 10,
      grid: false,
      x: {label: "Player Assisted: ", tickRotate: -30},
      y: {label: "Assists to Omar Marmoush"},
      color: {legend: false},
      marks: [
      Plot.dot(assisted, { x: "player_assisted", y: "id", r: "id", fill: "gold", stroke: "red" }),
        Plot.arrow(assisted, {
      x1: "player_assisted",
      y1: 0,
      x2: "player_assisted",
      y2: "id",
      bend: true,
      stroke: "brown"
    }) ,
        Plot.text(assisted, {
      x: "player_assisted",
      y: "id",
      text: "player_assisted",
      fill: "gold",
      stroke: "red",
      dy: 15,
      rotate:-45
    }),
      Plot.tip(assisted, Plot.pointerY({x: "player_assisted", y: "id"}))
      ]})
      )
  }</div>
</div>

```js
const action = FileAttachment("action.csv").csv({typed: true});
//view(Inputs.table(action))
const minutes = FileAttachment("minute.csv").csv({typed: true});
const assisted = FileAttachment("assisted.csv").csv({typed: true});
const result = FileAttachment("result.csv").csv({typed: true});
```

<!-- ```js
view(Inputs.table(data));
``` -->
Desarrollo: Enrique A Lopez Magallón - [@EnriqueALopezM](https://twitter.com/EnriqueALopezM)