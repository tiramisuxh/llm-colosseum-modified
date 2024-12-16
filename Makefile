run:
	diambra -r C:\Users\su_xi\.diambra\roms run -l python script.py

demo:
	diambra -r ~/.diambra/roms run -l python3 demo.py && python3 result.py

local:
	diambra -r ~/.diambra/roms run -l python3 local.py

install:
	pip3 install -r requirements.txt

go:
	while true; do make run; done