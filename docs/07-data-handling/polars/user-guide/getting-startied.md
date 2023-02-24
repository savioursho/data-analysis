
- <a href="#getting-started" id="toc-getting-started">Getting started</a>
  - <a href="#installation" id="toc-installation">Installation</a>
  - <a href="#quick-start" id="toc-quick-start">Quick start</a>
  - <a href="#lazy-quick-start" id="toc-lazy-quick-start">Lazy quick
    start</a>
  - <a href="#polars-quick-exploration-guide"
    id="toc-polars-quick-exploration-guide">Polars quick exploration
    guide</a>
    - <a href="#installation-and-import"
      id="toc-installation-and-import">Installation and Import</a>
    - <a href="#object-creation" id="toc-object-creation">Object creation</a>
    - <a href="#viewing-data" id="toc-viewing-data">Viewing data</a>
    - <a href="#expressions" id="toc-expressions">Expressions</a>
    - <a href="#combining-dataframes" id="toc-combining-dataframes">Combining
      dataframes</a>

# Getting started

[Getting started - Polars - User
Guide](https://pola-rs.github.io/polars-book/user-guide/quickstart/intro.html)

### Installation

``` console
$ pip install polars
```

### Quick start

``` python
import polars as pl

df = pl.read_csv("https://j.mp/iriscsv")
df.head() # html format
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (5, 5)</small>
<thead>
<tr>
<th>
sepal_length
</th>
<th>
sepal_width
</th>
<th>
petal_length
</th>
<th>
petal_width
</th>
<th>
species
</th>
</tr>
<tr>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
str
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
5.1
</td>
<td>
3.5
</td>
<td>
1.4
</td>
<td>
0.2
</td>
<td>
&quot;setosa&quot;
</td>
</tr>
<tr>
<td>
4.9
</td>
<td>
3.0
</td>
<td>
1.4
</td>
<td>
0.2
</td>
<td>
&quot;setosa&quot;
</td>
</tr>
<tr>
<td>
4.7
</td>
<td>
3.2
</td>
<td>
1.3
</td>
<td>
0.2
</td>
<td>
&quot;setosa&quot;
</td>
</tr>
<tr>
<td>
4.6
</td>
<td>
3.1
</td>
<td>
1.5
</td>
<td>
0.2
</td>
<td>
&quot;setosa&quot;
</td>
</tr>
<tr>
<td>
5.0
</td>
<td>
3.6
</td>
<td>
1.4
</td>
<td>
0.2
</td>
<td>
&quot;setosa&quot;
</td>
</tr>
</tbody>
</table>
</div>

``` python
print(df.head()) # print format
```

    shape: (5, 5)
    ┌──────────────┬─────────────┬──────────────┬─────────────┬─────────┐
    │ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width ┆ species │
    │ ---          ┆ ---         ┆ ---          ┆ ---         ┆ ---     │
    │ f64          ┆ f64         ┆ f64          ┆ f64         ┆ str     │
    ╞══════════════╪═════════════╪══════════════╪═════════════╪═════════╡
    │ 5.1          ┆ 3.5         ┆ 1.4          ┆ 0.2         ┆ setosa  │
    │ 4.9          ┆ 3.0         ┆ 1.4          ┆ 0.2         ┆ setosa  │
    │ 4.7          ┆ 3.2         ┆ 1.3          ┆ 0.2         ┆ setosa  │
    │ 4.6          ┆ 3.1         ┆ 1.5          ┆ 0.2         ┆ setosa  │
    │ 5.0          ┆ 3.6         ┆ 1.4          ┆ 0.2         ┆ setosa  │
    └──────────────┴─────────────┴──────────────┴─────────────┴─────────┘

``` python
(df.filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum()))
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (3, 5)</small>
<thead>
<tr>
<th>
species
</th>
<th>
sepal_length
</th>
<th>
sepal_width
</th>
<th>
petal_length
</th>
<th>
petal_width
</th>
</tr>
<tr>
<td>
str
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;setosa&quot;
</td>
<td>
116.9
</td>
<td>
81.7
</td>
<td>
33.2
</td>
<td>
6.1
</td>
</tr>
<tr>
<td>
&quot;versicolor&quot;
</td>
<td>
281.9
</td>
<td>
131.8
</td>
<td>
202.9
</td>
<td>
63.3
</td>
</tr>
<tr>
<td>
&quot;virginica&quot;
</td>
<td>
324.5
</td>
<td>
146.2
</td>
<td>
273.1
</td>
<td>
99.6
</td>
</tr>
</tbody>
</table>
</div>

### Lazy quick start

``` python
# 実行されない
(pl.read_csv("https://j.mp/iriscsv")
    .lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
)
```

<i>naive plan: (run <b>LazyFrame.describe_optimized_plan()</b> to see the optimized plan)</i>
    <p></p>
    <div>  Aggregate<p></p>     [col("sepal_length").sum(), col("sepal_width").sum(), col("petal_length").sum(), col("petal_width").sum()] BY [col("species")] FROM<p></p>        FILTER [(col("sepal_length")) > (5i32)] FROM<p></p>    DF ["sepal_length", "sepal_width", "petal_length", "petal_width"]; PROJECT */5 COLUMNS; SELECTION: "None"<p></p><p></p></div>

``` python
# .collect()で実行される
(pl.read_csv("https://j.mp/iriscsv")
    .lazy()
    .filter(pl.col("sepal_length") > 5)
    .groupby("species", maintain_order=True)
    .agg(pl.all().sum())
    .collect()
)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (3, 5)</small>
<thead>
<tr>
<th>
species
</th>
<th>
sepal_length
</th>
<th>
sepal_width
</th>
<th>
petal_length
</th>
<th>
petal_width
</th>
</tr>
<tr>
<td>
str
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;setosa&quot;
</td>
<td>
116.9
</td>
<td>
81.7
</td>
<td>
33.2
</td>
<td>
6.1
</td>
</tr>
<tr>
<td>
&quot;versicolor&quot;
</td>
<td>
281.9
</td>
<td>
131.8
</td>
<td>
202.9
</td>
<td>
63.3
</td>
</tr>
<tr>
<td>
&quot;virginica&quot;
</td>
<td>
324.5
</td>
<td>
146.2
</td>
<td>
273.1
</td>
<td>
99.6
</td>
</tr>
</tbody>
</table>
</div>

## Polars quick exploration guide

[Polars quick exploration guide - Polars - User
Guide](https://pola-rs.github.io/polars-book/user-guide/quickstart/quick-exploration-guide.html)

### Installation and Import

``` console
pip install -U polars
```

``` python
import polars as pl
from datetime import datetime, timedelta
import numpy as np
```

### Object creation

#### From scratch

`Series`

``` python
series = pl.Series(
    "a", [1, 2, 3, 4, 5]
)
series
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (5,)</small>
<thead>
<tr>
<th>
a
</th>
</tr>
<tr>
<td>
i64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
</tr>
<tr>
<td>
2
</td>
</tr>
<tr>
<td>
3
</td>
</tr>
<tr>
<td>
4
</td>
</tr>
<tr>
<td>
5
</td>
</tr>
</tbody>
</table>
</div>

``` python
series = pl.Series(
    [1, 2, 3, 4, 5]
)
series
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (5,)</small>
<thead>
<tr>
<th>

</th>
</tr>
<tr>
<td>
i64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
</tr>
<tr>
<td>
2
</td>
</tr>
<tr>
<td>
3
</td>
</tr>
<tr>
<td>
4
</td>
</tr>
<tr>
<td>
5
</td>
</tr>
</tbody>
</table>
</div>

``` python
type(series)
```

    polars.internals.series.series.Series

``` python
isinstance(series, pl.Series)
```

    True

`Dataframe`

``` python
dataframe = pl.DataFrame({
    "integer": [1, 2, 3],
    "date":[
        (datetime(2022, 1, 1)),
        (datetime(2022, 1, 2)),
        (datetime(2022, 1, 3)),
    ],
    "float": [4.0, 5.0, 6.0],
})
dataframe
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (3, 3)</small>
<thead>
<tr>
<th>
integer
</th>
<th>
date
</th>
<th>
float
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
2022-01-01 00:00:00
</td>
<td>
4.0
</td>
</tr>
<tr>
<td>
2
</td>
<td>
2022-01-02 00:00:00
</td>
<td>
5.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
2022-01-03 00:00:00
</td>
<td>
6.0
</td>
</tr>
</tbody>
</table>
</div>

``` python
type(dataframe)
```

    polars.internals.dataframe.frame.DataFrame

``` python
isinstance(dataframe, pl.DataFrame)
```

    True

#### From file

##### csv

``` python
dataframe.write_csv("output.csv")
```

``` python
df_csv = pl.read_csv("output.csv")
df_csv
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (3, 3)</small>
<thead>
<tr>
<th>
integer
</th>
<th>
date
</th>
<th>
float
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
str
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
&quot;2022-01-01T00:...
</td>
<td>
4.0
</td>
</tr>
<tr>
<td>
2
</td>
<td>
&quot;2022-01-02T00:...
</td>
<td>
5.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
&quot;2022-01-03T00:...
</td>
<td>
6.0
</td>
</tr>
</tbody>
</table>
</div>

paarse dates

``` python
df_csv_with_dates = pl.read_csv("output.csv", parse_dates=True)
df_csv_with_dates
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (3, 3)</small>
<thead>
<tr>
<th>
integer
</th>
<th>
date
</th>
<th>
float
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
1
</td>
<td>
2022-01-01 00:00:00
</td>
<td>
4.0
</td>
</tr>
<tr>
<td>
2
</td>
<td>
2022-01-02 00:00:00
</td>
<td>
5.0
</td>
</tr>
<tr>
<td>
3
</td>
<td>
2022-01-03 00:00:00
</td>
<td>
6.0
</td>
</tr>
</tbody>
</table>
</div>

### Viewing data

We first create a `DataFrame` to work with.

``` python
df = pl.DataFrame({
    "a": np.arange(0, 8),
    "b": np.random.rand(8),
    "c": [
        datetime(2022, 12, 1) + timedelta(days=idx)
        for idx in range(8)
    ],
    "d": [1, 2.0, np.nan, np.nan, 0, -5, -42, None],
})
df
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
</tr>
</tbody>
</table>
</div>

`head`

``` python
df.head()
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (5, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
</tr>
</tbody>
</table>
</div>

`tail`

``` python
df.tail()
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (5, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
</tr>
</tbody>
</table>
</div>

`sample`

``` python
df.sample(n=3)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (3, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
</tr>
</tbody>
</table>
</div>

`describe`

``` python
df.describe()
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (7, 5)</small>
<thead>
<tr>
<th>
describe
</th>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
str
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
str
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;count&quot;
</td>
<td>
8.0
</td>
<td>
8.0
</td>
<td>
&quot;8&quot;
</td>
<td>
8.0
</td>
</tr>
<tr>
<td>
&quot;null_count&quot;
</td>
<td>
0.0
</td>
<td>
0.0
</td>
<td>
&quot;0&quot;
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
&quot;mean&quot;
</td>
<td>
3.5
</td>
<td>
0.469427
</td>
<td>
null
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
&quot;std&quot;
</td>
<td>
2.44949
</td>
<td>
0.3044
</td>
<td>
null
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
&quot;min&quot;
</td>
<td>
0.0
</td>
<td>
0.004543
</td>
<td>
&quot;2022-12-01 00:...
</td>
<td>
-42.0
</td>
</tr>
<tr>
<td>
&quot;max&quot;
</td>
<td>
7.0
</td>
<td>
0.977514
</td>
<td>
&quot;2022-12-08 00:...
</td>
<td>
2.0
</td>
</tr>
<tr>
<td>
&quot;median&quot;
</td>
<td>
3.5
</td>
<td>
0.429145
</td>
<td>
null
</td>
<td>
1.0
</td>
</tr>
</tbody>
</table>
</div>

### Expressions

#### Select statement

select all columns

``` python
df.select(
    pl.col("*")
)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
</tr>
</tbody>
</table>
</div>

``` python
print(pl.col("*"))
print(type(pl.col("*")))
```

    *
    <class 'polars.internals.expr.expr.Expr'>

select specific columns

``` python
df.select(
    pl.col(["a", "b"])
)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 2)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
</tr>
</tbody>
</table>
</div>

``` python
df.select([
    pl.col("a"),
    pl.col("b")
])
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 2)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
</tr>
</tbody>
</table>
</div>

What if column names are duplicated?

It raises exception.

``` python
try:
    df.select(
        pl.col(["a", "a"])
    )
except Exception as e:
    print(e)
```

    Column with name: 'a' has more than one occurrences

exclude columns

``` python
df.select([
    pl.exclude("a")
])
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 3)</small>
<thead>
<tr>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
</tr>
<tr>
<td>
0.256279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
0.415364
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
</tr>
<tr>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
</tr>
<tr>
<td>
0.808474
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
</tr>
</tbody>
</table>
</div>

#### Filter

``` python
df.filter(
    pl.col("c")
    .is_between(
        datetime(2022, 12, 2), datetime(2022, 12, 8),
        closed = "none",
    ),
)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (5, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
</tr>
</tbody>
</table>
</div>

``` python
df.filter(
    (pl.col("a") <= 3) &
    (pl.col("d").is_not_nan())
)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (2, 4)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
</tr>
</tbody>
</table>
</div>

#### With_columns

``` python
df.with_columns([
    pl.col("b").sum().alias("e"),
    (pl.col("b") + 42).alias("b+42"),
])
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 6)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
<th>
e
</th>
<th>
b+42
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
<td>
f64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
<td>
3.755417
</td>
<td>
42.442926
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
<td>
3.755417
</td>
<td>
42.368511
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
<td>
3.755417
</td>
<td>
42.256279
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
<td>
3.755417
</td>
<td>
42.977514
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
<td>
3.755417
</td>
<td>
42.004543
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
<td>
3.755417
</td>
<td>
42.415364
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
<td>
3.755417
</td>
<td>
42.481805
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
<td>
3.755417
</td>
<td>
42.808474
</td>
</tr>
</tbody>
</table>
</div>

#### Groupby

``` python
df2 = pl.DataFrame({
    "x": np.arange(0, 8),
    "y": ["A", "A", "A", "B", "B", "C", "X", "X"],
})
df2
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 2)</small>
<thead>
<tr>
<th>
x
</th>
<th>
y
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
str
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
1
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
2
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
3
</td>
<td>
&quot;B&quot;
</td>
</tr>
<tr>
<td>
4
</td>
<td>
&quot;B&quot;
</td>
</tr>
<tr>
<td>
5
</td>
<td>
&quot;C&quot;
</td>
</tr>
<tr>
<td>
6
</td>
<td>
&quot;X&quot;
</td>
</tr>
<tr>
<td>
7
</td>
<td>
&quot;X&quot;
</td>
</tr>
</tbody>
</table>
</div>

``` python
df2.groupby(
    "y", maintain_order=True
).count()
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (4, 2)</small>
<thead>
<tr>
<th>
y
</th>
<th>
count
</th>
</tr>
<tr>
<td>
str
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;A&quot;
</td>
<td>
3
</td>
</tr>
<tr>
<td>
&quot;B&quot;
</td>
<td>
2
</td>
</tr>
<tr>
<td>
&quot;C&quot;
</td>
<td>
1
</td>
</tr>
<tr>
<td>
&quot;X&quot;
</td>
<td>
2
</td>
</tr>
</tbody>
</table>
</div>

What if `maintain_order=False`

``` python
df2.groupby(
    "y", maintain_order=False
).count()
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (4, 2)</small>
<thead>
<tr>
<th>
y
</th>
<th>
count
</th>
</tr>
<tr>
<td>
str
</td>
<td>
u32
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;C&quot;
</td>
<td>
1
</td>
</tr>
<tr>
<td>
&quot;X&quot;
</td>
<td>
2
</td>
</tr>
<tr>
<td>
&quot;A&quot;
</td>
<td>
3
</td>
</tr>
<tr>
<td>
&quot;B&quot;
</td>
<td>
2
</td>
</tr>
</tbody>
</table>
</div>

``` python
df2.groupby("y", maintain_order=True).agg([
    pl.col("*").count().alias("count"),
    pl.col("*").sum().alias("sum"),
])
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (4, 3)</small>
<thead>
<tr>
<th>
y
</th>
<th>
count
</th>
<th>
sum
</th>
</tr>
<tr>
<td>
str
</td>
<td>
u32
</td>
<td>
i64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
&quot;A&quot;
</td>
<td>
3
</td>
<td>
3
</td>
</tr>
<tr>
<td>
&quot;B&quot;
</td>
<td>
2
</td>
<td>
7
</td>
</tr>
<tr>
<td>
&quot;C&quot;
</td>
<td>
1
</td>
<td>
5
</td>
</tr>
<tr>
<td>
&quot;X&quot;
</td>
<td>
2
</td>
<td>
13
</td>
</tr>
</tbody>
</table>
</div>

#### Combining operations

``` python
df_x = df.with_column(
    (pl.col("a") * pl.col("b")).alias("a * b")
).select([
    pl.all().exclude(["c", "d"])
])
df_x
```

    /tmp/ipykernel_7851/499404871.py:1: DeprecationWarning: `with_column` has been deprecated in favor of `with_columns`. This method will be removed in version 0.17.0
      df_x = df.with_column(

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 3)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
a * b
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
f64
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.442926
</td>
<td>
0.0
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.368511
</td>
<td>
0.368511
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.256279
</td>
<td>
0.512558
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.977514
</td>
<td>
2.932543
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.004543
</td>
<td>
0.018172
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.415364
</td>
<td>
2.076821
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.481805
</td>
<td>
2.890832
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.808474
</td>
<td>
5.659321
</td>
</tr>
</tbody>
</table>
</div>

### Combining dataframes

#### Join

``` python
df = pl.DataFrame({"a": np.arange(0, 8), 
                   "b": np.random.rand(8), 
                   "c": [datetime(2022, 12, 1) + timedelta(days=idx) for idx in range(8)],
                   "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
                  })

df2 = pl.DataFrame({
                    "x": np.arange(0, 8), 
                    "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X'],
})
```

``` python
df.join(
    df2, left_on="a", right_on="x",
)
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 5)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
<th>
y
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
<td>
str
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.384484
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.455516
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.527279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.81465
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
<td>
&quot;B&quot;
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.716841
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
<td>
&quot;B&quot;
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.359398
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
<td>
&quot;C&quot;
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.901799
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
<td>
&quot;X&quot;
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.274225
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
<td>
&quot;X&quot;
</td>
</tr>
</tbody>
</table>
</div>

#### Concat

``` python
pl.concat([df, df2], how="horizontal")
```

<div>
<style>
.pl-dataframe > thead > tr > th {
  text-align: right;
}
</style>

<table border="1" class="pl-dataframe">
<small>shape: (8, 6)</small>
<thead>
<tr>
<th>
a
</th>
<th>
b
</th>
<th>
c
</th>
<th>
d
</th>
<th>
x
</th>
<th>
y
</th>
</tr>
<tr>
<td>
i64
</td>
<td>
f64
</td>
<td>
datetime[μs]
</td>
<td>
f64
</td>
<td>
i64
</td>
<td>
str
</td>
</tr>
</thead>
<tbody>
<tr>
<td>
0
</td>
<td>
0.384484
</td>
<td>
2022-12-01 00:00:00
</td>
<td>
1.0
</td>
<td>
0
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
1
</td>
<td>
0.455516
</td>
<td>
2022-12-02 00:00:00
</td>
<td>
2.0
</td>
<td>
1
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
2
</td>
<td>
0.527279
</td>
<td>
2022-12-03 00:00:00
</td>
<td>
NaN
</td>
<td>
2
</td>
<td>
&quot;A&quot;
</td>
</tr>
<tr>
<td>
3
</td>
<td>
0.81465
</td>
<td>
2022-12-04 00:00:00
</td>
<td>
NaN
</td>
<td>
3
</td>
<td>
&quot;B&quot;
</td>
</tr>
<tr>
<td>
4
</td>
<td>
0.716841
</td>
<td>
2022-12-05 00:00:00
</td>
<td>
0.0
</td>
<td>
4
</td>
<td>
&quot;B&quot;
</td>
</tr>
<tr>
<td>
5
</td>
<td>
0.359398
</td>
<td>
2022-12-06 00:00:00
</td>
<td>
-5.0
</td>
<td>
5
</td>
<td>
&quot;C&quot;
</td>
</tr>
<tr>
<td>
6
</td>
<td>
0.901799
</td>
<td>
2022-12-07 00:00:00
</td>
<td>
-42.0
</td>
<td>
6
</td>
<td>
&quot;X&quot;
</td>
</tr>
<tr>
<td>
7
</td>
<td>
0.274225
</td>
<td>
2022-12-08 00:00:00
</td>
<td>
null
</td>
<td>
7
</td>
<td>
&quot;X&quot;
</td>
</tr>
</tbody>
</table>
</div>
