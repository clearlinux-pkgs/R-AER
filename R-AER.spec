#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-AER
Version  : 1.2.5
Release  : 1
URL      : https://cran.r-project.org/src/contrib/AER_1.2-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/AER_1.2-5.tar.gz
Summary  : Applied Econometrics with R
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-Formula
Requires: R-car
Requires: R-lmtest
Requires: R-pbkrtest
Requires: R-plm
Requires: R-sandwich
Requires: R-systemfit
Requires: R-zoo
BuildRequires : R-Formula
BuildRequires : R-car
BuildRequires : R-lmtest
BuildRequires : R-pbkrtest
BuildRequires : R-plm
BuildRequires : R-sandwich
BuildRequires : R-systemfit
BuildRequires : R-zoo
BuildRequires : clr-R-helpers

%description
Christian Kleiber and Achim Zeileis (2008),
	     Applied Econometrics with R, Springer-Verlag, New York.
	     ISBN 978-0-387-77316-2. (See the vignette "AER" for a package overview.)

%prep
%setup -q -c -n AER

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521216803

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521216803
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library AER
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library AER
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library AER
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library AER|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/AER/CITATION
/usr/lib64/R/library/AER/DESCRIPTION
/usr/lib64/R/library/AER/INDEX
/usr/lib64/R/library/AER/Meta/Rd.rds
/usr/lib64/R/library/AER/Meta/data.rds
/usr/lib64/R/library/AER/Meta/demo.rds
/usr/lib64/R/library/AER/Meta/features.rds
/usr/lib64/R/library/AER/Meta/hsearch.rds
/usr/lib64/R/library/AER/Meta/links.rds
/usr/lib64/R/library/AER/Meta/nsInfo.rds
/usr/lib64/R/library/AER/Meta/package.rds
/usr/lib64/R/library/AER/Meta/vignette.rds
/usr/lib64/R/library/AER/NAMESPACE
/usr/lib64/R/library/AER/NEWS
/usr/lib64/R/library/AER/R/AER
/usr/lib64/R/library/AER/R/AER.rdb
/usr/lib64/R/library/AER/R/AER.rdx
/usr/lib64/R/library/AER/data/Affairs.rda
/usr/lib64/R/library/AER/data/ArgentinaCPI.rda
/usr/lib64/R/library/AER/data/BankWages.rda
/usr/lib64/R/library/AER/data/BenderlyZwick.rda
/usr/lib64/R/library/AER/data/BondYield.rda
/usr/lib64/R/library/AER/data/CASchools.rda
/usr/lib64/R/library/AER/data/CPS1985.rda
/usr/lib64/R/library/AER/data/CPS1988.rda
/usr/lib64/R/library/AER/data/CPSSW04.rda
/usr/lib64/R/library/AER/data/CPSSW3.rda
/usr/lib64/R/library/AER/data/CPSSW8.rda
/usr/lib64/R/library/AER/data/CPSSW9204.rda
/usr/lib64/R/library/AER/data/CPSSW9298.rda
/usr/lib64/R/library/AER/data/CPSSWEducation.rda
/usr/lib64/R/library/AER/data/CartelStability.rda
/usr/lib64/R/library/AER/data/ChinaIncome.rda
/usr/lib64/R/library/AER/data/CigarettesB.rda
/usr/lib64/R/library/AER/data/CigarettesSW.rda
/usr/lib64/R/library/AER/data/CollegeDistance.rda
/usr/lib64/R/library/AER/data/ConsumerGood.rda
/usr/lib64/R/library/AER/data/CreditCard.rda
/usr/lib64/R/library/AER/data/DJFranses.rda
/usr/lib64/R/library/AER/data/DJIA8012.rda
/usr/lib64/R/library/AER/data/DoctorVisits.rda
/usr/lib64/R/library/AER/data/DutchAdvert.rda
/usr/lib64/R/library/AER/data/DutchSales.rda
/usr/lib64/R/library/AER/data/Electricity1955.rda
/usr/lib64/R/library/AER/data/Electricity1970.rda
/usr/lib64/R/library/AER/data/EquationCitations.rda
/usr/lib64/R/library/AER/data/Equipment.rda
/usr/lib64/R/library/AER/data/EuroEnergy.rda
/usr/lib64/R/library/AER/data/Fatalities.rda
/usr/lib64/R/library/AER/data/Fertility.rda
/usr/lib64/R/library/AER/data/Fertility2.rda
/usr/lib64/R/library/AER/data/FrozenJuice.rda
/usr/lib64/R/library/AER/data/GSOEP9402.rda
/usr/lib64/R/library/AER/data/GSS7402.rda
/usr/lib64/R/library/AER/data/GermanUnemployment.rda
/usr/lib64/R/library/AER/data/GoldSilver.rda
/usr/lib64/R/library/AER/data/GrowthDJ.rda
/usr/lib64/R/library/AER/data/GrowthSW.rda
/usr/lib64/R/library/AER/data/Grunfeld.rda
/usr/lib64/R/library/AER/data/Guns.rda
/usr/lib64/R/library/AER/data/HMDA.rda
/usr/lib64/R/library/AER/data/HealthInsurance.rda
/usr/lib64/R/library/AER/data/HousePrices.rda
/usr/lib64/R/library/AER/data/Journals.rda
/usr/lib64/R/library/AER/data/KleinI.rda
/usr/lib64/R/library/AER/data/Longley.rda
/usr/lib64/R/library/AER/data/MASchools.rda
/usr/lib64/R/library/AER/data/MSCISwitzerland.rda
/usr/lib64/R/library/AER/data/ManufactCosts.rda
/usr/lib64/R/library/AER/data/MarkDollar.rda
/usr/lib64/R/library/AER/data/MarkPound.rda
/usr/lib64/R/library/AER/data/Medicaid1986.rda
/usr/lib64/R/library/AER/data/Mortgage.rda
/usr/lib64/R/library/AER/data/MotorCycles.rda
/usr/lib64/R/library/AER/data/MotorCycles2.rda
/usr/lib64/R/library/AER/data/Municipalities.rda
/usr/lib64/R/library/AER/data/MurderRates.rda
/usr/lib64/R/library/AER/data/NMES1988.rda
/usr/lib64/R/library/AER/data/NYSESW.rda
/usr/lib64/R/library/AER/data/NaturalGas.rda
/usr/lib64/R/library/AER/data/OECDGas.rda
/usr/lib64/R/library/AER/data/OECDGrowth.rda
/usr/lib64/R/library/AER/data/OlympicTV.rda
/usr/lib64/R/library/AER/data/OrangeCounty.rda
/usr/lib64/R/library/AER/data/PSID1976.rda
/usr/lib64/R/library/AER/data/PSID1982.rda
/usr/lib64/R/library/AER/data/PSID7682.rda
/usr/lib64/R/library/AER/data/Parade2005.rda
/usr/lib64/R/library/AER/data/PepperPrice.rda
/usr/lib64/R/library/AER/data/PhDPublications.rda
/usr/lib64/R/library/AER/data/ProgramEffectiveness.rda
/usr/lib64/R/library/AER/data/RecreationDemand.rda
/usr/lib64/R/library/AER/data/ResumeNames.rda
/usr/lib64/R/library/AER/data/SIC33.rda
/usr/lib64/R/library/AER/data/STAR.rda
/usr/lib64/R/library/AER/data/ShipAccidents.rda
/usr/lib64/R/library/AER/data/SmokeBan.rda
/usr/lib64/R/library/AER/data/SportsCards.rda
/usr/lib64/R/library/AER/data/StrikeDuration.rda
/usr/lib64/R/library/AER/data/SwissLabor.rda
/usr/lib64/R/library/AER/data/TeachingRatings.rda
/usr/lib64/R/library/AER/data/TechChange.rda
/usr/lib64/R/library/AER/data/TradeCredit.rda
/usr/lib64/R/library/AER/data/TravelMode.rda
/usr/lib64/R/library/AER/data/UKInflation.rda
/usr/lib64/R/library/AER/data/UKNonDurables.rda
/usr/lib64/R/library/AER/data/USAirlines.rda
/usr/lib64/R/library/AER/data/USConsump1950.rda
/usr/lib64/R/library/AER/data/USConsump1979.rda
/usr/lib64/R/library/AER/data/USConsump1993.rda
/usr/lib64/R/library/AER/data/USCrudes.rda
/usr/lib64/R/library/AER/data/USGasB.rda
/usr/lib64/R/library/AER/data/USGasG.rda
/usr/lib64/R/library/AER/data/USInvest.rda
/usr/lib64/R/library/AER/data/USMacroB.rda
/usr/lib64/R/library/AER/data/USMacroG.rda
/usr/lib64/R/library/AER/data/USMacroSW.rda
/usr/lib64/R/library/AER/data/USMacroSWM.rda
/usr/lib64/R/library/AER/data/USMacroSWQ.rda
/usr/lib64/R/library/AER/data/USMoney.rda
/usr/lib64/R/library/AER/data/USProdIndex.rda
/usr/lib64/R/library/AER/data/USSeatBelts.rda
/usr/lib64/R/library/AER/data/USStocksSW.rda
/usr/lib64/R/library/AER/data/WeakInstrument.rda
/usr/lib64/R/library/AER/data/datalist
/usr/lib64/R/library/AER/demo/Ch-Basics.R
/usr/lib64/R/library/AER/demo/Ch-Intro.R
/usr/lib64/R/library/AER/demo/Ch-LinearRegression.R
/usr/lib64/R/library/AER/demo/Ch-Microeconometrics.R
/usr/lib64/R/library/AER/demo/Ch-Programming.R
/usr/lib64/R/library/AER/demo/Ch-TimeSeries.R
/usr/lib64/R/library/AER/demo/Ch-Validation.R
/usr/lib64/R/library/AER/doc/AER.R
/usr/lib64/R/library/AER/doc/AER.Rnw
/usr/lib64/R/library/AER/doc/AER.pdf
/usr/lib64/R/library/AER/doc/Sweave-journals.R
/usr/lib64/R/library/AER/doc/Sweave-journals.Rnw
/usr/lib64/R/library/AER/doc/Sweave-journals.pdf
/usr/lib64/R/library/AER/doc/index.html
/usr/lib64/R/library/AER/help/AER.rdb
/usr/lib64/R/library/AER/help/AER.rdx
/usr/lib64/R/library/AER/help/AnIndex
/usr/lib64/R/library/AER/help/aliases.rds
/usr/lib64/R/library/AER/help/paths.rds
/usr/lib64/R/library/AER/html/00Index.html
/usr/lib64/R/library/AER/html/R.css
