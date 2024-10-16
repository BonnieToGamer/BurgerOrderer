# Burger Orderer
Group 20's assignment

Available Makefile Commands:

<code>make build</code>
Builds the Docker containers defined in the compose.yaml file. This command should be run before trying to execute or test the application.

<code>make run</code>
Runs the application using the Docker containers specified in the compose.yaml file.

<code>make test</code>
Runs the application with additional containers for testing using both compose.yaml and compose.test.yaml files. This will:

* Start the containers.
* Run the tests in the test containers.
* Print logs for the burger_orderer_test_container and kitchen_view_test_container.

<code>make clean</code>

Stops and removes all running containers, networks, and volumes defined in both the compose.yaml and compose.test.yaml files. Use this command to clean up resources after testing or running the application.

<code>make help</code>

Displays a help message that summarizes the available Makefile commands.

File Overview:

* compose.yaml: Defines the services and configurations for running the main application.
* compose.test.yaml: Defines additional services and configurations for running the test environment.


Notes:
* The test target will stop the test containers automatically after the tests have completed, using the --abort-on-container-exit and -t 0 flags.
* To view recent logs from the test containers, the docker logs command is used with a 5-second filter for relevant output. (This is arbitrary random number that can and should change.)