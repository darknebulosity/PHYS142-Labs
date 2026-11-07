import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd 
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.stats as stats
    from scipy.optimize import curve_fit
    from uncertainties import ufloat, nominal_value, std_dev

    return curve_fit, np, pd, plt, stats


@app.cell
def _(pd):
    data = pd.DataFrame({
        "brass1": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [8.2, 16.1, 24, 31.7, 39.6],
                "19": [7.1, 14.4, 21.4, 28.5, 35.7],
                "17": [6.4, 12.7, 19.2, 25.7, 31.7],
                "15": [5.8, 11.2, 17, 22.4, 27.9],
                "13": [5.2, 9.7, 14.5, 19.6, 24.3]
            },
            "length": 29.2, # CENTIMETERS
            "mass": 0.4, # GRAMS
            "resistance": [],
     		"diameter": .51 # MILLIMETERS
            },
        "brass2": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [2.9, 5.9, 8.8, 11.9, 14.8],
                "19": [2.6, 5.3, 7.9, 10.6, 13.4],
                "17": [2.3, 4.9, 7.2, 9.5, 11.8],
                "15": [2.1, 4.2, 6.3, 8.3, 10.4],
                "13": [1.9, 3.7, 5.4, 7.2, 9.1]
            },
            "length": 29.3,
            "mass": 1.2,
            "resistance": [],
     		"diameter": .81
            },
        "brass3": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [1.8, 3.5, 5.4, 7.1, 8.9],
                "19": [1.6, 3.2, 4.9, 6.4, 8.0],
                "17": [1.4, 2.9, 4.3, 5.7, 7.2],
                "15": [1.2, 2.5, 3.8, 5.1, 6.3],
                "13": [1.2, 2.3, 3.4, 4.5, 5.6]
            },
            "length": 29.2,
            "mass": 1.9,
            "resistance": [],
     		"diameter": 1

            },
        "brass4": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [1.3, 2.4, 3.6, 4.7, 6],
                "19": [1.1, 2.2, 3.3, 4.3, 5.4],
                "17": [1, 2, 2.9, 3.9, 4.8],
                "15": [0.9, 1.7, 2.5, 3.4, 4.3],
                "13": [0.8, 1.5, 2.2, 2.9, 3.6]
            },
            "length": 29.2,
            "mass": 3.1,
            "resistance": [],
     		"diameter": 1.3

            },
        "white": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [1.4, 2.9, 4.3, 5.7, 7.1],
                "15": [1.1, 2.1, 3.1, 4.1, 5.2],
            },
            "length": 29.2,
            "mass": 0.5,
            "resistance": [],
     		"diameter": 1

            },
        "red": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [0.5, 0.9, 1.4, 1.9, 2.3],
                "15": [0.4, 0.7, 1, 1.3, 1.7],
            },
            "length": 29.3,
            "mass": 1.89,
            "resistance": [],
     		"diameter": 1
            },
        "silver": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [27.2, 53.4, 79.2, 105.5, 131.9],
                "15": [19.1, 38.1, 57.1, 75.9, 93.8],
            },
            "length": 29.2,
            "mass": 1.8,
            "resistance": [],
     		"diameter": 1
            },
        "dirty": {
            "current": [0.1, 0.2, 0.3, 0.4, 0.5],
            "voltage": {
                "21": [19.4, 40, 59.2, 79.4, 99.5],
                "15": [13.9, 28.7, 42.4, 55.9, 70.3],
            },
            "length": 29.2,
            "mass": 1.8,
            "resistance": [],
     		"diameter": 1
            },

    })

    results = pd.DataFrame({
        "brass1": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "brass2": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "brass3": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "brass4": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "white": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "red": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "silver": {
            "resistivity": 0.0,
            "density": 0.0
        },
        "dirty": {
            "resistivity": 0.0,
            "density": 0.0
        }




    })
    results
    return data, results


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Resistance Relationship $R \propto l/{d^{2}}$
    """)
    return


@app.cell
def _(data, stats):
    # first calculate resistance values


    ## i can probably actually use this to find the resistivity

    # CODE OVERVIEW: first get all of the brass columns. then set up a dictionary of EVERY possible datapoint, put it into [res], [distance], [diameter]. the trial will be organized by the index. 

    # then, iterate through every brass column. in every brass column, iterate through every distance, whose elements contain a voltage measurement.
    # then, take a linear regression (since R = V/I) and get the slope of the curve, which will be the resistance. append the resistance to the resistance key, append distance to the distance key, and append the diameter to the diameter key

    brass_cols = [col for col in data.columns if "brass" in col]

    brass_data = []
    brass_alt = {
        "res": [],
        "distance": [],
     	"diameter": [],
    }

    for wire in brass_cols:
        y_data = []
        data.loc["resistance_error", wire] = []
        data.at["resistance_fit", wire] = {
            "21": 0,
            "19": 0,
            "17": 0,
            "15": 0,
            "13": 0
        }

        for distance in data[wire].voltage:

            regression = stats.linregress(data[wire].current, data[wire].voltage[distance])
            data.at["resistance_fit", wire][distance] = regression
    
            #print(f"R({distance})={regression.slope}")
            y_data.append(regression.slope) # add every R value to the regression

            brass_alt["res"].append(regression.slope)
            brass_alt["distance"].append(float(distance))
            brass_alt["diameter"].append(data[wire].diameter)

            #print(data.loc["resistance", wire])

            data.loc["resistance", wire].append(regression.slope)
            data.loc["resistance_error", wire].append(regression.stderr)

        #data.loc["resistance_error", wire] = np.average(data.loc["resistance_error", wire][data.loc["resistance_error", wire] != 0])


    data.T
         # returns resistance (ohms), distance (meters), diameter (meters)

    #brass_alt
    return brass_alt, brass_cols


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Graphs for I against V - no regression
    """)
    return


@app.cell
def _(brass_cols, data, plt):
    for _distance in data["brass1"].voltage:
        print(_distance)

        for _wire in brass_cols:
            #print(list(data[_wire]["resistance"]))
            plt.errorbar(data[_wire].current, data[_wire].voltage[_distance], fmt="o", xerr=.01, yerr=.1, ms=5, label=f'{data[_wire].diameter}mm wire')
    
    

        plt.xlabel("Current (A)")
        plt.ylabel("Voltage (mV)")
        plt.legend()
        plt.show()
        print('-------------')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Graphs for I against V - regression
    """)
    return


@app.cell
def _(brass_cols, data, np, plt):
    for _distance in data["brass1"].voltage:
        print(_distance)

        for _wire in brass_cols:
            #print(list(data[_wire]["resistance"]))
            plt.errorbar(data[_wire].current, data[_wire].voltage[_distance], fmt="o", xerr=.01, yerr=0.1, ms=5, label=f'{data[_wire].diameter}mm wire')
    
    
            _x=np.linspace(0,0.5)
            plt.plot(_x, data.at["resistance_fit", _wire][_distance][0] * _x + data.at["resistance_fit", _wire][_distance][1])        

        plt.xlabel("Current (A)")
        plt.ylabel("Voltage (mV)")
        plt.legend()
        plt.savefig(f"{int(_distance)} brass.png", bbox_inches="tight", dpi=300)

        plt.show()
        print('-------------')
    return


@app.cell(hide_code=True)
def _(brass_cols, data, plt):
    for _wire in brass_cols:
        print(len(list(data[_wire]["resistance"])))
        print(len(list(data[_wire].voltage.keys())))

        plt.errorbar([float(x) for x in list(data[_wire].voltage.keys())], data[_wire]["resistance"], fmt="o", xerr=.1, yerr=1, ms=5)

    plt.xlabel("Distance")
    plt.ylabel("Resistance")
    plt.show()

    for _wire in brass_cols:

        plt.errorbar(5*[data[_wire].diameter], data[_wire]["resistance"], fmt="o", yerr=1, ms=5, label=f'{data[_wire].diameter}mm brass wire')

    plt.xlabel("Distance (cm)")
    plt.ylabel("Resistance (µΩ)")
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Actually calculating relationship
    """)
    return


@app.cell
def _(brass_alt, curve_fit, data, np):
    def resistance_function(vars, resistivity, alpha, beta):
        # vars is defined as [length, diameter]
        length = vars[0]
        diameter = vars[1]

        return resistivity * np.power(length, alpha) /  np.power(diameter, beta)

    distances = [float(x) for x in list(data.brass1.voltage.keys())] # convert distances to a list in centiMETERS

    fit = curve_fit(f= resistance_function, xdata= [brass_alt["distance"], brass_alt["diameter"]], ydata= brass_alt["res"])

    #fit = curve_fit(resistance_function, [distances, 5*[(data.brass1.diameter)/1000]], y_data)

    popt, pcov = fit

    resistivity, alpha, beta = popt 

    print(f"Constant = {resistivity}, alpha = {alpha}, beta = {beta}")
    print(f"Std error: {np.sqrt(np.diag(pcov))}")

    print(f"{resistivity}")
    return distances, popt, resistance_function


@app.cell
def _(
    brass_alt,
    brass_cols,
    data,
    distances,
    np,
    plt,
    popt,
    resistance_function,
):
    for index, _distance in enumerate(distances):
        for _wire in brass_cols:
            _x_err = np.sqrt( (1/(data[_wire]["diameter"] / 10)* 0.14 )**2 + (2 / ((data[_wire]["diameter"]) / 10)**3 * 0.01 *((data[_wire]["diameter"]) / 10)) ** 2 )
    
            plt.errorbar(_distance * float(data[_wire]["diameter"])**-2, data[_wire]["resistance"][index], fmt="o", xerr=_x_err, yerr=1, ms=5, label=f'd={data[_wire]["diameter"]}, l={_distance}cm')


        #print(resistance_function([_distance, brass_alt["diameter"]], *popt))


            #print(_distance)


        plt.plot(_distance * np.power(brass_alt["diameter"], -2), resistance_function([_distance, brass_alt["diameter"]], *popt) )
        plt.xlabel(r"Ratio $\frac{l}{d^2}$", fontsize=15)
        plt.ylabel(r"Resistance ($\mu\Omega$)", fontsize=15)
        plt.legend()
        plt.savefig(f"{int(_distance)} ratio.png", bbox_inches="tight", dpi=300)

        plt.show()




    #print(resistance_function([13, brass_alt["diameter"]], *popt))

    data
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Calculating Resistivity of each wire

    $\rho ={\frac{RA}{L}}$

    1. For Each Wire
        - For Each Voltage (different distances)
            - Calculate Resistance (curve fit)
    2. Calculate $\rho$ based on $RA/L$.
        - Average them
    """)
    return


@app.cell
def _(data, np, results, stats):
    data_dupe = data # never hurts to be safe

    for _wire in data_dupe:
        print(_wire)
        resistivity_array = []
        data_dupe.loc["resistance_error", _wire] = []
        data_dupe.loc["area_error", _wire] = []
        data_dupe.loc["length_error", _wire] = []



        for _distance in data_dupe[_wire].voltage:

            milli_v = [volt / 1000 for volt in data_dupe[_wire].voltage[_distance]]
            v = [volt for volt in data_dupe[_wire].voltage[_distance]]
            _regression = stats.linregress(data_dupe[_wire].current, milli_v) # the slope of this line is R

            micro_ohm = _regression.slope * 10**(6)
            diameter_cm = (data_dupe[_wire].diameter / 10)

            area_new = np.pi * ((diameter_cm / 2) ** 2)

            # calculate resistivity
            resistivity_array.append(micro_ohm * area_new / (float(_distance))) # the _distance is the distance between the probes. we do NOT divide by length

            data_dupe.loc["area_error", _wire].append(((_regression.slope / float(_distance)) * (np.pi / 200 * diameter_cm ** 2)))
            data_dupe.loc["length_error", _wire].append((_regression.slope * area_new / float(_distance)**2) * 0.14 )
            data_dupe.loc["resistance_error", _wire].append((area_new/float(_distance)*(_regression.stderr)))



           # area = np.pi * ((data_dupe[_wire].diameter / 1000) / 2) ** 2 
           # _resistivity = _regression.slope * area / (data_dupe[_wire].length / 100)

        area_avg_err = np.average(data_dupe.loc["area_error", _wire]) 
        length_avg_err = np.average(data_dupe.loc["length_error", _wire]) 
        res_avg_err = np.average(data_dupe.loc["resistance_error", _wire]) 


        #print([area_avg_err, length_avg_err, res_avg_err])

        resistivity_err = np.sqrt(area_avg_err ** 2 + length_avg_err ** 2 + res_avg_err **2) * 10**6

        #data_dupe.loc["resistivity_error", _wire] = np.sqrt()

        print(f"resistivity avg: {np.average(resistivity_array)}, err {resistivity_err}")


        results.at["resistivity",_wire] = np.average(resistivity_array)
        results.at["res_err", _wire] = resistivity_err
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Finding Density of Wires
    """)
    return


@app.cell
def _(data, np, results):
    for _wire in data:
        #print(_wire)

        volume = np.pi * (data[_wire].diameter /10 / 2) ** 2 * data[_wire].length 

        density = data[_wire].mass / volume
        #print(f"Density: {density}")


        results.at["density",_wire] = density

        unc_mass = 0.1
        unc_volume = np.sqrt(( (np.pi/2) * (data[_wire].diameter /10)**2 * 1/100   )**2 + (np.pi / 4 * (data[_wire].diameter /10)**2 * 0.1)**2 )

        err_mass = (1/volume *unc_mass)
        err_volume = (data[_wire].mass / volume**2 * unc_volume)
        err_density = np.sqrt(err_mass**2 + err_volume**2)

        results.at["density_err",_wire] = err_density


        print(err_density)



    results.T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    White: Aluminum alloy (because low density, and resistivity around 4.9)

    Red: Copper. Density of 8.21, resistivity of 1.69 which is pretty okay with our error

    Silver: Nichrome. Resistivity around ~100, density of 8.3

    Dirty: Not sure. Could be stainless steel, 304, or invar. **Leaning towards 304** because lower end of resistvity, and higher end of density.
    """)
    return


if __name__ == "__main__":
    app.run()
