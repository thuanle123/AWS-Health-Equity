# health_equity_hackathon_bmf
Program to extra BMF data

The names of the columns you are required to capture from the BMF data are:
* EIN
* NAME and/or SORT_NAME
* STREET
* CITY
* ZIP
* ACTIVITY
* NTEE_CD
* REVENUE_AMT

There are two types of service classification codes used in the BMF data that describe the types of services provided by an organization: Activity codes and NTEE codes. Some rows of the BMF file include only one type of code, some have both, and some have neither. Furthermore, there can be multiple codes of each type. For activity codes, there can be up to three assigned so you’ll find either three, six, or nine digits in the CSV field. If you wish to learn more about these service classification codes, the category names and codes are listed in the aforementioned PDF about the BMF data, but NTEE categories have descriptions available at a dedicated website. As previously mentioned, organizations that have been assigned categories which are not relevant to Johego users can be filtered out of the dataset. Johego has provided a whitelist of NTEE codes and a whitelist of Activity codes, both in CSV format hosted on S3. The whitelist of NTEE codes uses a shorthand such that the entry “E2” represents inclusion of the NTEE category “E20” as well as all of its sub-categories. If any of the Activity codes or NTEE codes assigned to an organization are found in the respective whitelist, the organization should be included in the final dataset.
