# Equipment Status
An docker container with [Flask](http://flask.pocoo.org/). It's used to simply update and view broken equipment within Platoon DJs.
## Prereqs
In order to run the image, [Docker](https://www.docker.com/) is reqiured.
## Setup
There are two ways of building the image. First, clone the repo:     
`git clone https://github.com/platoon-djs/equipment-status.git`      
Enter the folder: `cd equipment-status`.

**Recommended build:** the easiest way is to use make:   
```make build```

**Manual build:** if you want to build it yourself you can do so:     
```docker build -t equipment-status .```

### Running
To run the container; use:     
`make run`     
or      
```docker run -p 5000:5000 -d -v `pwd`/app/:/var/www/ equipment-status```

Stuff should now be running at [http://localhost:5000](http://localhost:5000). 
To manage reports, visit [http://localhost:5000/manage](http://localhost:5000/manage).


