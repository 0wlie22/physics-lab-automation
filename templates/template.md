<div style="align: right">\VAR{author}</div>

## Aprēķini

### Tiešo mērījumu kļūdas aprēķins

1. Vidējā aritmētiskā vērtība:

${\VAR{value}}_{vid} = \frac1{\VAR{length}} \sum\limits^{\VAR{length}}_{i=1} {\VAR{value}}_i = \VAR{average}$

2. Vidējā kvadrātiskā kļūda:

$s_{\VAR{value}} = \sqrt{\frac{\sum\limits^{\VAR{length}}_{i=1} {\VAR{value}}_i - {\VAR{value}}_{vid}^2}{{\VAR{length}} (\VAR{length} - 1)}} = \VAR{squared_error}$

3. Rezultātu, kas satur rupju kļūdu izslēgšana

* Vidējā aritmētiskā vērtība:

    ${\VAR{value}}_{vid} = \frac1{\VAR{length}} \sum\limits^{\VAR{length}}_{i=1} {\VAR{value}}_i = \VAR{average}$

* Vidējā kvadrātiskā kļūda:

    $s_{\VAR{value}} = \sqrt{\frac{\sum\limits^{\VAR{length}}_{i=1} {\VAR{value}}_i - {\VAR{value}}_{vid}^2}{{\VAR{length}} (\VAR{length} - 1)}} = \VAR{squared_error}$

5. Absolūta kļūda:

$\Delta\VAR{value} = s_{\VAR{value}} * t_{0.95}(\VAR{length}) = \VAR{absolute_error}$

6. Relatīva kļūda:

$\varepsilon_{\VAR{value}}=\frac{\Delta \VAR{value}}{\VAR{value}_{vid}} = \VAR{relative_error}\%$

## Rezultāti

$\VAR{value} = \VAR{average} \pm \VAR{squared_error},\ \varepsilon = \VAR{relative_error}\% \ \ pie \ \beta=0.95$
