# QWealth Factor Research Demonstration

This repository contains code that showcases a sample factor-based research process for a risk-premia flavor factor research project. The notebooks are sequentially structured to guide you through data retrieval, modeling, strategy development, and performance attribution. Comments in each notebook explain the results and decision-making process.

## Repository Structure

The code files are organized as follows:

1. **0.0. Data_Retrival.ipynb**  
   Retrieves data from WRDS, following their best practices.

2. **1.0. Univariate_Modelling.ipynb**  
   Performs univariate modeling of Value and Momentum factors.

3. **1.1. Univariate_Modelling_w_Market_Control.ipynb**  
   (Optional) Extends univariate modeling of Value and Momentum with market returns as a control variable.

4. **2.0. Multivariate_Modeling.ipynb**  
   Conducts multivariate modeling of Value, Momentum, and Market factors.

5. **3.0. Strategy.ipynb**  
   Develops a backtest strategy based on the model created in multivariate modeling.

6. **4.0. Performance_Attribution.ipynb**  
   Analyzes performance attribution and risk analysis on the backtested portfolio returns using Fama-French 3 factors.

## Research Approach

The notebooks follow a step-by-step research process, showcasing the methods and interpretations for factor research.

- **Custom Bucket Plots:** Each notebook contains custom bucket plots to illustrate linearity, monotonicity, and fit of the factors.
  
- **Stability Assessment:** Cumulative beta returns are used to assess factor stability, while fitted vs actual and fitted vs residual plots help to examine model fit.
  
- **Regression Techniques:** Rolling regressions and traditional endogenous cross-sectional regressions are employed to fit coefficients, with detailed notes on their interpretations and limitations.

- **Portfolio Strategy:** A basic Long/Short (L/S) portfolio is constructed and backtested using the models from the multivariate analysis. Though the results are limited, metrics for assessment are provided.

- **Risk Exposure Analysis:** The final notebook, 4.0, provides a framework for evaluating the portfolio's risk exposure through Fama-French 3-factor analysis on returns.

## Limitations and Considerations

- **Data Quality:** Due to time constraints, a more thorough data review was not conducted. Some results suggest the presence of extremes, leverage points, and/or outliers. Given more time, I would explore windsorizing or filtering out extreme points to refine the analysis.

- **Factor Simplicity:** The simplicity of the factors used contributes to the limitations in model performance. Although data from WRDS is assumed to be of high quality, further data cleansing could enhance accuracy. Results should be considered with this caveat in mind.

---

This repository provides a foundational framework for factor-based research and illustrates a sample approach to analyzing risk-premia factors.