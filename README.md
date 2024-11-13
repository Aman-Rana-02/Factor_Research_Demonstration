# QWealth Factor Research Demonstration

This repository contains code that showcases a sample factor-based research process for a risk-premia flavor factor research project. The notebooks are structured in sequence to guide readers through data retrieval, modeling, strategy development, and performance attribution. Each notebook includes comments that walk the reader through results and the reasoning behind decisions.

To note is that I do not use Fama-French's portfolio method to fit Betas, instead I fit Betas at a firm level, to better capture firm specific sensitivities.

## Repository Structure

The code files are ordinally named as follows:

1. **0.0. Data_Retrival.ipynb**  
   Holds code retrieving data from WRDS, following their best practices.

2. **1.0. Univariate_Modelling.ipynb**  
   Univariate modeling of Value and Momentum.

3. **1.1. Univariate_Modelling_w_Market_Control.ipynb**  
   (Optional) Univariate modeling of Value and Momentum in context with market returns.

4. **2.0. Multivariate_Modeling.ipynb**  
   Multivariate modeling of Value, Momentum, and the Market.

5. **3.0. Strategy.ipynb**  
   A strategy backtest based on the model developed.

6. **4.0. Performance_Attribution.ipynb**  
   Performance attribution and risk analysis on the backtest portfolio’s returns.

## Research Approach

The goal of this task was to showcase a research process for a risk-premia factor project. Each notebook is filled with comments that explain decisions and results at each stage.

- **Custom Bucket Plots:** To illustrate linearity, monotonicity, and fit, the notebooks contain custom bucket plots.
  
- **Stability Assessment:** Cumulative beta returns highlight factor stability, while fitted vs actual and fitted vs residual plots showcase model fit.
  
- **Regression Techniques:** Rolling regressions and traditional endogenous cross-sectional regressions are used to fit coefficients, with notes explaining interpretations and caveats.

- **Portfolio Strategy:** A basic Long/Short (L/S) portfolio is built and presented using the models developed in 2.0. The results are expectedly poor, but metrics for assessment are included.

- **Risk Exposure Analysis:** Notebook 4.0 provides a framework using Fama-French 3 factors to assess portfolio risk exposure by analyzing returns.

## Real-World Implementation Notes

Research outcome: Value in this form is weak, simple Momentum is stronger, but they are still insufficient on their own to explain a significant variation in firm-specific returns.

I use OLS in the research process here, this assumes normal returns, and the shortfalls of this approach is clear in the fitted vs actual plots. What this tangibly means is that the model will systematically underrepresent large market moves in the upside or downside, and an additional risk management layer would preferably be developed on top of the market allocation. 

The strategy rebalances at a monthly frequency.

The Risk Exposure Analysis can be used to finetune portfolios to better adhere to risk factor exposure (Value, Momentum, Profitability) mandates.

## Limitations and Considerations

- **Data Quality:** A more robust review of the data itself would be ideal. Some model results suggest the presence of extremes, leverage points, and/or outliers. Given more time, I would consider windsorizing or removing such points as appropriate.

- **Factor Simplicity:** The results are limited by the simplicity of the factors, as well as potential data issues noted above. Although WRDS data is generally clean, it’s worth caveating the results accordingly.

---

This repository illustrates a foundational framework for factor-based research, offering an end-to-end walkthrough of risk-premia factor analysis with a straightforward approach to data, models, and strategy development.
