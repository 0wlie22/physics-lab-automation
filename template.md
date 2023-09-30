
## Aprēķini

### Tiešo mērījumu kļūdas aprēķins

1. Vidējā aritmētiskā vērtība: 

${<value>}_{vid} = \frac1{<length>} \sum^{<length>}_{i=1} {<value>}_i = <average>$ 

2. Vidējā kvadrātiskā kļūda:

$s_{<value>} = \sqrt{\frac{\sum\limits^{<length>}_{i=1} {<value>}_i - {<value>}_{vid}^2}{{<length>} (<length> - 1)}} = <squared_error>$

3. Rezultātu, kas satur rupju kļūdu izslēgšana

* Vidējā aritmētiskā vērtība: 

    ${<value>}_{vid} = \frac1{<length>} \sum^{<length>}_{i=1} {<value>}_i = <average>$ 

* Vidējā kvadrātiskā kļūda:

    $s_{<value>} = \sqrt{\frac{\sum\limits^{<length>}_{i=1} {<value>}_i - {<value>}_{vid}^2}{{<length>} (<length> - 1)}} = <squared_error>$

5. Absolūta kļūda:

$\Delta<value> = s_{<value>} * t_{0.95}(<length>) = <absolute_error>$

6. Relatīva kļūda:

$\varepsilon_{<value>}=\frac{\Delta <value>}{<value>_{vid}} = <relative_error>\%$

## Rezultāti

$<value> = <average> \pm <squared_error>,\ \varepsilon = <relative_error>\% \ \ pie \ \beta=0.95$
