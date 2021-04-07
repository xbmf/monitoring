# Website Monitoring

The solution consists of 2 main services called `consumer` and `producer`.

### Prerequisites

- Python 3.7.x
- Necessary environment variables files and certificate.

### Implementation

Basic micro-services principles are followed.

`consumer` is responsible from consuming the KAFKA queue, and persist the log into the Postgre Database.

`producer` service is responsible from creating task to check the website availability and producing metrics to the
Kafka topic

There is also another component called `scheduler` which is responsible for scheduling check website tasks.

If you want to add more website to monitor, simply edit the file `producer/fixtures/websites.json` file.

### Assumptions

- There is nothing specified about how the target website will be defined. I assumed it'll be defined in a static
  resource file (`producer/fixtures/websites.json`)
- I assumed the monitor will check the website in a constant time interval (in seconds) `see: website.interval`
- I assumed necessary components as postgresql and kafka will be ready on aiven platform `see: .env.test, .env.dev`

### Pre-Install

It would be good to install the packages in a virtual environment or use a tool like miniconda

```bash
conda create --name aiven-homework python=3.7
conda activate aiven-homework
```

### Install

Simply run the following command:

```bash
make install
```

### Tests

Simply run the following command:

```bash
make test
```

### Run

To run all the services, just run the following command:

```bash
sh run.sh
```

### Improvement

- Actually, I didn't like my implementation of consumer kafka. It is currently using an infinite loop, and it is not a
  good way to handle this kind of consuming operations. I would like to implement with async principles if I had more
  time.
- I would like to create another folder called `integration-tests` and write the real integration tests for consumer and
  producer service.
- I would like to implement kafka consumer & producer more abstractly and write a contract testing in each separate
  service, if I had more time.
