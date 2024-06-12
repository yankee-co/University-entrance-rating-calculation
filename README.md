# Entrance rating place calculation

This console application was processing Ukrainian University rating pages and calculating your probable place in the lists for different choosen specialities and theirs faculties.
I used it before applying on wanted specialities and its faculties to see where I would have higher chances (my rating was ~ 180) as a result I got budget place, where I expected it.

## Why this scipt was needed and used ?
- There were a lot of preferential (or priveleged) entrants that were completely messing up the general list and your demonstrated place on it, so the information wasn't actual at all.

### Output examples:

![image](https://github.com/yankee-co/University-entrance-rating-calculation/assets/72886859/8cd6adb0-b2f4-481e-bc5a-40d5ea68044b)

![image](https://github.com/yankee-co/University-entrance-rating-calculation/assets/72886859/b4947282-745b-4e91-88f4-9877631ec1ac)

### Values meaning

121-126 - Specialty id,
1-5 priorities (in which place in entrant list this speciality and its faculty is placed, everyone could sumbit up to five applications for admission, so if there's were a lot with 4 - 5 above you, they are most likely aren't your concurrents, the program was giving that information so user could understand more precisely his chances),
bigger numbers right next to priorities - quantity of people with corresponding priority.
General place - your probable place in the list.

Script was also counting people that had 'Recommended' tag in the list as those who likely wil be included.

173.5 is rating used in the program (max is 200)

![image](https://github.com/yankee-co/University-entrance-rating-calculation/assets/72886859/76b43cec-b79c-4693-886e-5a7de5b97392)

So script was analyzing the whole list and building for you another from zero counting every person with higher rating than given to the program and showing priority of their choice and not counting previleged that woudn't be inluded bacause they were beyond the limit (max quantity of previlged entrants) and their rating were lower than yours.
