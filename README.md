# basic-form-detection
made in python

METHOD 1:
bug check:
possible counter measure against code:
putting bogus "<form" by using comment in source
multiple "<form" will cause code to phreak/break.
solution to counter measure:
1) use reGex module
2) MechanicalSoup / BeautifulSoup

another solution without using modules.
sanitary check by finding "<input" in the form list, we need to do this because all we need is to find the payload so we can test vulnerability

possible countermeasure on "No Module" solution:
commented / bogus "input" element in the form list.
This may cause problem when we start a request with a payload that's not used because it's bogus and it has no use
whether or not requests will still work with a bogus payload is up to me since i haven't tested it, i'm simply thinking

possible counter measure to bogus element(aka comments)
do loops on html source so we can sanity check for bogus element(commented elements.)
this is useful when we are dealing with a coder who LOVESS to explain simply BASIC GODDAMN THING in his CODE. (aka a huge chunk of useless information lying in your target code that won't be used by a MACHINE, only by you.)
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
METHOD 2:
removed comments, easy form detect. very line-short.
In conclusion, it's flexible but NOT that flexible.
used reGex module.

method 1 is way flexible but very line-long.

                                                                                                            To @Maddam Huissen
