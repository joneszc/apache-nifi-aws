build:
	docker build -t mxsdata/nifi-toolkit ./nifi-toolkit
	docker build -t mxsdata/nifi ./nifi
	#docker build --network=host -t mxsdata/nifi-toolkit ./nifi-toolkit
	#docker build --network=host -t mxsdata/nifi ./nifi
