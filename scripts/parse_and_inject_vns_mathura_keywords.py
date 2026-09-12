import os
import re

raw_vns_data = """
kashi vishwanath mandir vip darshan
is there any special darshan in kashi vishwanath temple
bharat gaurav train kashi yatra from bangalore
kasi tour package from trichy by train
kashi vishwanath temple tour package
hubli to kashi tour package
varanasi and ayodhya itinerary
vizag to kasi trip
sightseeing varanasi
nirmala travels kashi yatra by flight price
varanasi to ayodhya package
varanasi trip package from bangalore
bangalore to kashi trip package
varanasi temple vip darshan
mathura vrindavan varanasi ayodhya tour package
hyderabad to kashi package
kashi yatra details
buddha tourism india
package tour to varanasi from bangalore
varanasi ayodhya tour package from kerala
kashi yatra from hyderabad
varanasi tours and travels
kashi vishwanath temple darshan booking online
kasi tourism
varanasi tourist package
mumbai to varanasi trip plan
varanasi tour package from chennai
varanasi prayagraj tour package
varanasi tour package from bangalore
bangalore to varanasi flight package
delhi varanasi ayodhya tour package
varanasi sightseeing tour package
varanasi darshan bus
varanasi tour package from kolkata by train
kashi vishwanath package
kashi vishwanath temple varanasi vip darshan
kasi yatra from bangalore
kasi yatra from chennai by train
kasi vishwakathar temple varanasi vip darshan
travel to kashi vishwanath
varanasi 3 days tour package
package trip to varanasi from bangalore
varanasi trip from delhi
ayodhya kashi tour
ayodhya varanasi tour package from bangalore
varanasi ayodhya prayagraj itinerary
irctc kasi package from bangalore
kashi darshan train package
benaras tour
book sugam darshan kashi vishwanath
nirmala travels kashi trip
nirmala travels kashi package
package for kashi vishwanath temple
tour operators in varanasi
kasi tour package from chennai gt holidays
banaras per head price
kasi tour package from kerala by flight
kashi vishwanath temple darshan ticket
nirmala travels kashi yatra by flight
sightseeing in varanasi
banaras package
irctc kasi tour package from chennai by train
adigas yatra kashi package price from bangalore
banaras trip package
varanasi prayagraj ayodhya tour package price
varanasi day trip
kashi banaras tour package
2 night 3 days varanasi itinerary
pune to varanasi trip plan
varanasi to darjeeling tour package
bangalore to kasi flight package
tamilnadu tourism kasi tour package price
kashi vishwanath online vip darshan booking
varanasi ayodhya prayagraj bodhgaya tour package
tour package from varanasi to ayodhya
kashi package from hyderabad
varanasi to ayodhya tour package price
kashi ayodhya prayagraj tour package from bangalore
varanasi tour package from pune
varanasi tour and travel company
kashi darshan tour package
kasi tour package from vizag
best kashi package from bangalore
varanasi tour in 2 days
bangalore to kashi package by flight
hyderabad to varanasi and ayodhya tour package
kashi tour
the memorable trip varanasi
kasi gaya tour package
varanasi ayodhya nepal tour package
varanasi tour package from bangalore by flight
banaras travel cost
varanasi to ayodhya trip
trip to ayodhya varanasi and prayagraj
irctc kashi yatra package
kolkata to varanasi tour packages
kashi tour package from bangalore by flight
tour and travel in varanasi
bangalore to varanasi tour packages
kaal bhairav temple varanasi vip darshan
kashi vip darshan pass
kashi vip darshan price
kashi yatra train
kashi local sightseeing
banaras tour and travels
varanasi travel itinerary
ayodhya and varanasi tour packages
kashi plan
banaras trip cost for 3 days
kashi travels varanasi
irctc kasi tour package from hyderabad
best travel agency kashi tour travels varanasi
benaras tour package from kolkata
kashi ayodhya prayagraj tour
dev diwali varanasi package
varanasi prayagraj ayodhya chitrakoot tour package price
varanasi tour package from kerala
ayodhya varanasi prayagraj tour package
varanasi and ayodhya tour package
package tour to varanasi
itinerary for banaras
kashi yatra package from hyderabad
bangalore to varanasi trip
banaras travel package
low budget varanasi trip
kashi ayodhya tour package from bangalore nirmala travels
pune to varanasi tour package
irctc varanasi tour package
varanasi gaya prayagraj ayodhya package tour
kashi ayodhya tour
visit kashi
varanasi package tour
varanasi ayodhya tour package price for family
nellore to kasi tour package
kasi gaya tour package from chennai by flight
varanasi trip cost for 3 days from kolkata
kashi ayodhya tour package from bangalore by train
trip to kasi from hyderabad
varanasi vip darshan price
lucknow ayodhya prayagraj varanasi tour package
kashi tour packages
tour package for ayodhya and varanasi
kashi packages from hyderabad
varanasi ayodhya prayagraj bodhgaya tour package
madurai to kasi tour package
benaras tour itinerary
ayodhya varanasi prayagraj tour kesari tours
kashi ayodhya tour package
varanasi darshan ticket
varanasi tour 1 day
varanasi to nepal tour packages by bus
varanasi tour package from kolkata
southern travels varanasi tour packages price
buddha gaya tour
varanasi local tour package
kashi gaya prayag ayodhya tour package price
varanasi ayodhya 3 days itinerary
kashi vishwanath mandir darshan booking
varanasi allahabad ayodhya naimisharanya tour package
bangalore to kashi package by kstdc
varanasi tour one day
kashi ayodhya tour package from mumbai
varanasi vrindavan ayodhya tour package
irctc kashi package
kasi flight package from chennai
kashi itinerary
banaras travels
varanasi tour package price
kashi varanasi tour package
kashi package tour
ayodhya varanasi itinerary
varanasi prayagraj ayodhya chitrakoot tour package
varanasi ayodhya package tour
tour and travels varanasi
travels in kashi
kashi vishwanath temple package
gaurav kashi darshan train
varanasi and ayodhya
varanasi and ayodhya tour
kasi tour package from vizag
kashi vishwanath tour guide
madurai to kasi train tour package
tours and travels varanasi
kashi darshan yatra
kashi trip from bangalore by train
ayodhya varanasi trip plan
varanasi local sightseeing package by car
ayodhya kashi vishwanath tour
ayodhya and varanasi tour
coimbatore to varanasi tour package
varanasi tour
free kasi tour
varanasi trips
kasi tour package from vijayawada
trip for varanasi
varanasi yatra package
package tours from varanasi
buddhist circuit tour package price
varanasi ayodhya mathura vrindavan tour package
kashi vip darshan
tour packages from varanasi
online vip darshan kashi vishwanath
kashi vishwanath tour guide
irctc kasi tour package from hyderabad
special darshan kashi vishwanath
irctc kasi tour package from trichy
banaras lucknow tour package
varanasi excursion
varanasi gaya prayagraj ayodhya package tour
irctc tour packages to varanasi
varanasi tour package for couple
banaras trip cost for 4 days
kashi vacations tour and travels
kashi vishwanath darshan booking
banaras trip
trip to varanasi from hyderabad
benaras tour plan
chennai to kasi flight package
varanasi tour package from varanasi
varanasi prayagraj ayodhya tour package price
kashi trip cost
tour packages in varanasi
buddha yatra
varanasi trip cost for 3 days
kashi sugam darshan booking
kasi tour package from pondicherry
varanasi local sightseeing package by bus
varanasi ayodhya tour package price
kashi vishwanath itinerary for 2 days
bodh gaya trip
varanasi to visit
package for kashi
bangalore to kashi package
kasi tour package from madurai by flight
varanasi 2 days tour package from delhi
kashi ayodhya tour and travels
varanasi tour and travel agency
kashi package from chennai
joshi tours and travels varanasi
ayodhya and banaras trip
varanasi asthi visarjan package
varanasi trip from delhi
varanasi day tour package
delhi to ayodhya and varanasi
trip to ayodhya and varanasi from delhi
kashi tours and travels varanasi
banaras trip cost
kashi vishwanath vip darshan price
tour package for ayodhya varanasi and prayagraj
kashi vishwanath temple package from bangalore
varanasi trip from kerala
varanasi ayodhya and prayagraj tour package
varanasi sightseeing cost
varanasi ram mandir tour package
kasi train package from chennai
sightseeing of banaras
irctc kashi package
kasi tour package from coimbatore by flight
buddhist circuit train ticket price
kasi tour from chennai by flight
manikarnika ghat tour
kashi package from delhi
varanasi allahabad ayodhya itinerary
kashi vishwanath itinerary
varanasi tour package for couple
kashi vishwanath mandir sparsh darshan
varanasi trip package
banaras couple trip
varanasi to ayodhya tour package
varanasi tour
kasi tour packages
ayodhya kashi mathura vrindavan tour package
varanasi tour package for family
ayodhya varanasi prayagraj tour packages
varanasi tour and travels tour packages
varanasi temple tour dasaswamedh ghat road lahori tola varanasi uttar pradesh
cruise service from kolkata to varanasi
varanasi ayodhya tour
kashi vishwanath trip cost
ayodhya and varanasi trip
prayagraj to varanasi tour package
kashiyatri
tours varanasi
varanasi to naimisharanya tour package
varanasi group tour packages
kashi tour package from mumbai
varanasi travel package
tour packages ayodhya varanasi
kashi vishwanath sightseeing
buddhist circuit tour
varanasi tour package from nagpur
tour package to varanasi
bangalore to varanasi package
local tour packages in varanasi
trip to ayodhya and varanasi
kasi yatra tour package from chennai
kashi banaras ayodhya trip
varanasi ayodhya tour package from bangalore
how to plan varanasi ayodhya trip
irctc kasi yatra
rv tours and travels kashi yatra package price
kashi package from mumbai
kasi viswanathar temple darshan booking
ayodhya kashi trip package
varanasi ayodhya tour package from mumbai
prayagraj ayodhya varanasi package
varanasi ayodhya tour plan
nirmala travels kashi yatra by flight from bangalore
irctc varanasi tour package from hyderabad by flight
kashi tour package from mangalore
banaras travel
varanasi trip from pune
varanasi prayagraj ayodhya tour package
pune to varanasi trip
varanasi itinerary
kashi vishwanath tour package
murugan travels kasi tour package
ayodhya kashi varanasi tour package
kashi trip plan from hyderabad
kashi tour packages from bangalore
delhi to ayodhya varanasi tour package
kashi trip from pune
kasi train tour package from coimbatore
irctc tour packages kashi
visit to varanasi
kashi ayodhya tour package from delhi
kasi trip package
varanasi to ayodhya tour
banaras trip from pune
delhi to kashi trip
irctc varanasi tour package from hyderabad
vishwanath darshan ticket
package tours from varanasi
pune to varanasi package
varanasi package
varanasi ayodhya tour package price
padharo kashi vacation
kashi tour package from bangalore
places to visit in varanasi with family
varanasi tour package from hyderabad by flight
shree kashi tour and travels
ayodhya kashi prayagraj itinerary
irctc kasi tour package from coimbatore
banaras tour plan from kolkata
bangalore to kasi package
varanasi to ayodhya one day tour package price
murugan travels kasi tour packages price
kashi tour package from bangalore by train
tourism in varanasi
kashi tours
kashi sightseeing package
banaras tour cost
varanasi gautam buddha temple
delhi to varanasi tour package
tour to banaras
varanasi travel
varanasi tour package from kerala
trip to kasi and ayodhya
dev deepawali varanasi tour package
varanasi trip from chennai
varanasi holiday packages
holiday in varanasi
banaras per person cost
varanasi prayagraj ayodhya chitrakoot tour itinerary
kashi trip packages
kashi vishwanath temple tour guide
varanasi honeymoon package
varanasi solo trip package
kashi vishwanath tourism
banaras vip darshan
ayodhya varanasi prayagraj tour package
kashi trip for senior citizens
hyderabad to kashi trip
kashi ayodhya trip
explore kashi
varanasi tour package from ahmedabad
gaya kashi vrindavan tour package
kashi vishwanath trip plan
varanasi tour plan
4 nights 5 days varanasi itinerary
madurai to kasi flight package
sparsh darshan at kashi vishwanath temple
varanasi to nepal package
kashi darshan tour and travels
dev deepawali tour package
kasi trip from vijayawada
kashi vishwanath temple tour
varanasi prayagraj ayodhya tour
kashi package tour
package for varanasi and ayodhya
banaras itinerary
ayodhya and kashi package from bangalore
varanasi tour from hyderabad
varanasi prayagraj tour package price
varanasi ram mandir tour package
divine touch tours
kasi gaya allahabad tour package
karnataka to kashi train package
trip to ayodhya varanasi and prayagraj
kashi trip package from bangalore
varanasi tours and travels
ayodhya prayagraj varanasi tour package from mumbai
kashi yatra package irctc
banaras trip 3 days
varanasi tour and travel
yava trip varanasi
varanasi khajuraho tour package
varanasi local sightseeing
kasi tours
banaras tour and travel
temple tour varanasi
nirmala travels kashi ayodhya tour package
ayodhya kashi prayagraj tour package
irctc kashi tour package from bangalore
varanasi tourist package
kashi ayodhya tour package from coimbatore
delhi to varanasi package
kashi temple package
prayagraj varanasi ayodhya tour package
varanasi trip from bangalore
varanasi trip from mumbai
salem to kasi tour packages
3 days varanasi itinerary
banaras trip cost for 5 days
kashi with anshu
ayodhya varanasi tour package
varanasi package
best varanasi tour package
kashi mathura vrindavan tour package price
varanasi package from bangalore
itinerary for kashi and ayodhya
kashi and ayodhya tour package from hyderabad
vip darshan in kashi vishwanath temple
tour package for varanasi and ayodhya
tour packages for varanasi
prayagraj varanasi ayodhya trip plan
varanasi tour package itinerary
varanasi ayodhya tour
kashi tour itinerary
varanasi ayodhya tour plan from kolkata
tour package from varanasi to ayodhya
heritage tours varanasi
delhi to varanasi tour
kasi trip from madurai
bangalore to kasi tour package
ayodhya varanasi tour
itinerary for ayodhya varanasi and prayagraj
kashi yatra package from mumbai
irctc varanasi tour package from delhi
travel agency for varanasi
banaras tour packages from mumbai
alaknanda cruise varanasi price
varanasi plan
varanasi 3 nights 4 days itinerary
kasi trip from coimbatore
visit in varanasi
kashi tour
kashi 9 days package from hyderabad
trip to kasi from chennai
kashi trip from bangalore
kashi vishwanath temple sparsh darshan booking
ayodhya kashi tour package
varanasi guided tours
varanasi package from chennai
trip plan for varanasi
kasi tour package from bangalore by flight price
kashi vishwanath temple package
kashi tour package from bangalore by train
how many days are enough for varanasi tour
banaras full trip package
varanasi package from hyderabad
irctc tour packages from hyderabad to varanasi
lucknow ayodhya varanasi tour package price
varanasi tour packages from hyderabad
kashi trip from hyderabad
varanasi full trip
kasi tour package from delhi
kashi trip from mumbai
nirmala travels varanasi package
varanasi itinerary 4 days
varanasi package from mumbai
chennai to varanasi flight tour package
banaras tour itinerary
prayagraj varanasi ayodhya tour
ayodhya varanasi tour package
amarnath ki yatra
miles of india best travel agency in varanasi varanasi tour packages reviews
kashi darshan package
trip to kasi from hyderabad
buddhist circuit in india
buddha trip
banaras tour plan
miles of india best travel agency in varanasi varanasi tour packages reviews
namo kashi tours & travel
ayodhya to varanasi tour
lucknow ayodhya varanasi tour
kashi tour package from pune
buddhist circuit tourist train
ayodhya kashi package
varanasi tour itinerary for 3 days
chennai to varanasi tour package by flight
kasi tour plan
varanasi prayagraj ayodhya chitrakoot tour package price
hyderabad to kasi trip plan
kasi viswanathar temple tour packages
banaras tour price
rv tours and travels kashi yatra package
kashi travel agency
chitragupta travels varanasi
varanasi to nepal tour package
trip to kashi vishwanath
varanasi to prayagraj one day tour package by bus
irctc kasi tour package
tour operator in varanasi
varanasi travel packages
kasi gaya allahabad tour package from coimbatore
kashi biswanath temple darshan
banaras kashi vishwanath darshan
beneras trip
tour packages from visakhapatnam to varanasi
bharat gaurav train from bangalore to kashi booking
banaras trip package
travel in varanasi
varanasi trip plan
varanasi ayodhya tour package
varanasi irctc package
ayodhya prayagraj tour
india tourism varanasi
kashi darshan yatra
ayodhya kashi varanasi tour package
varanasi visit plan
varanasi trip plan
ayodhya varanasi trip itinerary
banaras sight seeing
kasi tour package from rajahmundry
varanasi temple tour package
kashi ayodhya tour package
gaurav kashi yatra train
varanasi ayodhya prayagraj tour package
kashi tour package from pune
travels varanasi
kashi vip darshan booking
ayodhya varanasi tour packages
varanasi tour package from lucknow
varanasi local sightseeing package by bus timings
ayodhya varanasi tour
buddhist circuit tourist train ticket price
kashi prayagraj ayodhya tour package
varanasi group trip
varanasi tourism package
varanasi tour package from mumbai
prayagraj kashi ayodhya tour package
kasi viswanathar temple darshan
varanasi tour package from vijayawada
kashi vishwanath darshan online booking
kashi yatra package
kasi tour package from hyderabad
kashi triveni sangamam
kasi travel
kashi vishwanath vip darshan booking
kashi yatra tour package
kashi prayag ayodhya tour package
jatak travels varanasi
kashi package
tour packages from bangalore to varanasi
kashi ayodhya package
tour packages for varanasi
kasi trip package from chennai
buddhist tourist train
budget trip to varanasi
delhi to banaras trip
visit varanasi
one day tour in varanasi
how to plan kashi ayodhya and prayagraj
varanasi local tour operators
vip darshan at kashi vishwanath temple
tour package in varanasi
kashi vishwanath shringar darshan
ayodhya kashi vishwanath tour
ayodhya varanasi prayagraj tour package
trip to varanasi prayagraj and ayodhya
varanasi prayagraj ayodhya chitrakoot tour package price
varanasi prayagraj ayodhya tour package
banaras tour packages
irctc kashi ayodhya tour package from hyderabad
varanasi local tour package
kashi banaras tour package
varanasi 4 days tour package
banaras 2 day trip cost
kashi flight package
priya travels chandmari varanasi
varanasi ayodhya gaya tour package
sarnath tour guide
buddhist train
buddhist circuit tour package
bharat gaurav train from bangalore to kashi
itinerary for kashi vishwanath temple
varanasi tour from delhi
kashi ayodhya tour package from bangalore nirmala travels price
varanasi packages from hyderabad
varanasi to prayagraj tour package
chennai to varanasi tour package by train
kashi vishwanath tour
kashi tour package from mumbai
varanasi tour plan for 4 days
kashi tour package from ahmedabad
varanasi guided tour
kashi vishwanath budget trip
varanasi trip
plan varanasi trip
varanasi ayodhya prayagraj package
varanasi tour package from kathmandu
varanasi tour expenses
ayodhya varanasi prayagraj tour
kashi package
varanasi trip package from kerala
kolkata to banaras tour package
banaras ayodhya prayagraj tour
trip to kashi
pune to kashi tour package price
kasi tour package from coimbatore
boddh gaya package
varanasi trip planner
sarnath tour from varanasi
baba vishwanath vip darshan
tour of kashi babatpur reviews
kashi varanasi tours and travels
kashi temple package
varanasi tour and travels
bangalore to kashi package by kstdc price
ayodhya to varanasi tour package
varanasi prayagraj and ayodhya tour package
varanasi holiday
irctc holy kashi tour package
kashi yatra package
kashi ayodhya tour package from bangalore price
irctc kashi package
varanasi trip package
kashi vishwanath temple vip darshan
irctc varanasi tour package from chennai by train
hyderabad to varanasi tour packages
kasi tour package from chennai by train
southern travels varanasi
kashi mathura vrindavan ayodhya tour package
kashi varanasi tours and travels reviews
coimbatore to kasi tour package
kashi ayodhya tour package from bangalore
banaras trip price
kashi tour package from kerala
itinerary for kashi
vijayawada to kasi tour package
kashi darshan train
irctc varanasi tour package price
kashi tour package from bangalore by flight price
tourism in varanasi
kashi tours
kashi sightseeing package
banaras tour cost
varanasi gautam buddha temple
delhi to varanasi tour package
tour to banaras
varanasi travel
varanasi tour package from kerala
trip to kasi and ayodhya
dev deepawali varanasi tour package
varanasi trip from chennai
varanasi holiday packages
holiday in varanasi
banaras per person cost
varanasi prayagraj ayodhya chitrakoot tour itinerary
kashi trip packages
kashi vishwanath temple tour guide
varanasi honeymoon package
varanasi solo trip package
kashi vishwanath tourism
banaras vip darshan
ayodhya varanasi prayagraj tour package
kashi trip for senior citizens
hyderabad to kashi trip
kashi ayodhya trip
explore kashi
varanasi tour package from ahmedabad
gaya kashi vrindavan tour package
kashi vishwanath trip plan
varanasi tour plan
4 nights 5 days varanasi itinerary
madurai to kasi flight package
sparsh darshan at kashi vishwanath temple
varanasi to nepal package
kashi darshan tour and travels
dev deepawali tour package
kasi trip from vijayawada
kashi vishwanath temple tour
varanasi prayagraj ayodhya tour
kashi package tour
package for varanasi and ayodhya
banaras itinerary
ayodhya and kashi package from bangalore
varanasi tour from hyderabad
varanasi prayagraj tour package price
varanasi ram mandir tour package
divine touch tours
kasi gaya allahabad tour package
karnataka to kashi train package
trip to ayodhya varanasi and prayagraj
kashi trip package from bangalore
varanasi tours and travels
ayodhya prayagraj varanasi tour package from mumbai
kashi yatra package irctc
banaras trip 3 days
varanasi tour and travel
yava trip varanasi
varanasi khajuraho tour package
varanasi local sightseeing
kasi tours
banaras tour and travel
temple tour varanasi
nirmala travels kashi ayodhya tour package
ayodhya kashi prayagraj tour package
irctc kashi tour package from bangalore
varanasi tourist package
kashi ayodhya tour package from coimbatore
delhi to varanasi package
kashi temple package
prayagraj varanasi ayodhya tour package
varanasi trip from bangalore
varanasi trip from mumbai
salem to kasi tour packages
3 days varanasi itinerary
banaras trip cost for 5 days
kashi with anshu
ayodhya varanasi tour package
varanasi package
best varanasi tour package
kashi mathura vrindavan tour package price
varanasi package from bangalore
itinerary for kashi and ayodhya
kashi and ayodhya tour package from hyderabad
vip darshan in kashi vishwanath temple
tour package for varanasi and ayodhya
tour packages for varanasi
prayagraj varanasi ayodhya trip plan
varanasi tour package itinerary
varanasi ayodhya tour
kashi tour itinerary
varanasi ayodhya tour plan from kolkata
tour package from varanasi to ayodhya
heritage tours varanasi
delhi to varanasi tour
kasi trip from madurai
bangalore to kasi tour package
ayodhya varanasi tour
itinerary for ayodhya varanasi and prayagraj
kashi yatra package from mumbai
irctc varanasi tour package from delhi
travel agency for varanasi
banaras tour packages from mumbai
alaknanda cruise varanasi price
varanasi plan
varanasi 3 nights 4 days itinerary
kasi trip from coimbatore
visit in varanasi
kashi tour
kashi 9 days package from hyderabad
trip to kasi from chennai
kashi trip from bangalore
kashi vishwanath temple sparsh darshan booking
ayodhya kashi tour package
varanasi guided tours
varanasi package from chennai
trip plan for varanasi
kasi tour package from bangalore by flight price
kashi vishwanath temple package
kashi tour package from bangalore by train
how many days are enough for varanasi tour
banaras full trip package
varanasi package from hyderabad
irctc tour packages from hyderabad to varanasi
lucknow ayodhya varanasi tour package price
varanasi tour packages from hyderabad
kashi trip from hyderabad
varanasi full trip
kasi tour package from delhi
kashi trip from mumbai
nirmala travels varanasi package
varanasi itinerary 4 days
varanasi package from mumbai
chennai to varanasi flight tour package
banaras tour itinerary
prayagraj varanasi ayodhya tour
ayodhya varanasi tour package
amarnath ki yatra
miles of india best travel agency in varanasi varanasi tour packages reviews
kashi darshan package
trip to kasi from hyderabad
buddhist circuit in india
buddha trip
banaras tour plan
miles of india best travel agency in varanasi varanasi tour packages reviews
namo kashi tours & travel
ayodhya to varanasi tour
lucknow ayodhya varanasi tour
kashi tour package from pune
buddhist circuit tourist train
ayodhya kashi package
varanasi tour itinerary for 3 days
chennai to varanasi tour package by flight
kasi tour plan
varanasi prayagraj ayodhya chitrakoot tour package price
hyderabad to kasi trip plan
kasi viswanathar temple tour packages
banaras tour price
rv tours and travels kashi yatra package
kashi travel agency
chitragupta travels varanasi
varanasi to nepal tour package
trip to kashi vishwanath
varanasi to prayagraj one day tour package by bus
irctc kasi tour package
tour operator in varanasi
varanasi travel packages
kasi gaya allahabad tour package from coimbatore
kashi biswanath temple darshan
banaras kashi vishwanath darshan
beneras trip
tour packages from visakhapatnam to varanasi
bharat gaurav train from bangalore to kashi booking
banaras trip package
travel in varanasi
varanasi trip plan
varanasi ayodhya tour package
varanasi irctc package
ayodhya prayagraj tour
india tourism varanasi
kashi darshan yatra
ayodhya kashi varanasi tour package
varanasi visit plan
varanasi trip plan
ayodhya varanasi trip itinerary
banaras sight seeing
kasi tour package from rajahmundry
varanasi temple tour package
kashi ayodhya tour package
gaurav kashi yatra train
varanasi ayodhya prayagraj tour package
kashi tour package from pune
travels varanasi
kashi vip darshan booking
ayodhya varanasi tour packages
varanasi tour package from lucknow
varanasi local sightseeing package by bus timings
ayodhya varanasi tour
buddhist circuit tourist train ticket price
kashi prayagraj ayodhya tour package
varanasi group trip
varanasi tourism package
varanasi tour package from mumbai
prayagraj kashi ayodhya tour package
kasi viswanathar temple darshan
varanasi tour package from vijayawada
kashi vishwanath darshan online booking
kashi yatra package
kasi tour package from hyderabad
kashi triveni sangamam
kasi travel
kashi vishwanath vip darshan booking
kashi yatra tour package
kashi prayag ayodhya tour package
jatak travels varanasi
kashi package
tour packages from bangalore to varanasi
kashi ayodhya package
tour packages for varanasi
kasi trip package from chennai
buddhist tourist train
budget trip to varanasi
delhi to banaras trip
visit varanasi
one day tour in varanasi
how to plan kashi ayodhya and prayagraj
varanasi local tour operators
vip darshan at kashi vishwanath temple
tour package in varanasi
kashi vishwanath shringar darshan
ayodhya kashi vishwanath tour
ayodhya varanasi prayagraj tour package
trip to varanasi prayagraj and ayodhya
varanasi prayagraj ayodhya chitrakoot tour package price
varanasi prayagraj ayodhya tour package
banaras tour packages
irctc kashi ayodhya tour package from hyderabad
varanasi local tour package
kashi banaras tour package
varanasi 4 days tour package
banaras 2 day trip cost
kashi flight package
priya travels chandmari varanasi
varanasi ayodhya gaya tour package
sarnath tour guide
buddhist train
buddhist circuit tour package
bharat gaurav train from bangalore to kashi
itinerary for kashi vishwanath temple
varanasi tour from delhi
kashi ayodhya tour package from bangalore nirmala travels price
varanasi packages from hyderabad
varanasi to prayagraj tour package
chennai to varanasi tour package by train
kashi vishwanath tour
kashi tour package from mumbai
varanasi tour plan for 4 days
kashi tour package from ahmedabad
varanasi guided tour
kashi vishwanath budget trip
varanasi trip
plan varanasi trip
varanasi ayodhya prayagraj package
varanasi tour package from kathmandu
varanasi tour expenses
ayodhya varanasi prayagraj tour
kashi package
varanasi trip package from kerala
kolkata to banaras tour package
banaras ayodhya prayagraj tour
trip to kashi
pune to kashi tour package price
kasi tour package from coimbatore
boddh gaya package
varanasi trip planner
sarnath tour from varanasi
baba vishwanath vip darshan
tour of kashi babatpur reviews
kashi varanasi tours and travels
kashi temple package
varanasi tour and travels
bangalore to kashi package by kstdc price
ayodhya to varanasi tour package
varanasi prayagraj and ayodhya tour package
varanasi holiday
irctc holy kashi tour package
kashi yatra package
kashi ayodhya tour package from bangalore price
irctc kashi package
varanasi trip package
kashi vishwanath temple vip darshan
irctc varanasi tour package from chennai by train
hyderabad to varanasi tour packages
kasi tour package from chennai by train
southern travels varanasi
kashi mathura vrindavan ayodhya tour package
kashi varanasi tours and travels reviews
coimbatore to kasi tour package
kashi ayodhya tour package from bangalore
banaras trip price
kashi tour package from kerala
itinerary for kashi
vijayawada to kasi tour package
kashi darshan train
irctc varanasi tour package price
kashi tour package from bangalore by flight price
"""

# Extract unique keywords
lines = raw_vns_data.strip().split('\n')
extracted = set()

for l in lines:
    kw = l.strip()
    if kw and len(kw) > 2 and not kw.startswith("Search term") and not kw.startswith("All time"):
        extracted.add(re.sub(r'\s+', ' ', kw).lower())

vns_kw_list = sorted(list(extracted))
print(f"Total Unique Varanasi, Kashi & Braj Keywords Extracted: {len(vns_kw_list)}")

# Update parse_and_inject_jan_keywords.py to include these new terms
script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parse_and_inject_jan_keywords.py")

if os.path.exists(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        script_code = f.read()

    # Append new raw terms into the python script string
    new_terms_str = "\n".join(vns_kw_list)
    script_code = script_code.replace('"""\n\nlines = raw_data', f'\n{new_terms_str}\n"""\n\nlines = raw_data')
    
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(script_code)
    print("✅ Updated parse_and_inject_jan_keywords.py with all Varanasi, Kashi, Mathura & Vrindavan search terms!")
