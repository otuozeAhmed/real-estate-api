
## Real Estate API

This is a personalized dev project. However, you may use it whichever way you want in your personal project.

### How to set up...

####### To successfully set up this project ensure you have "Make" (Guide :- https://www.gnu.org/software/make/) and "Docker" (Guide :- https://docs.docker.com/engine/install/) installed in your Mac, Linux environment or WSL2 (Windows users), enter the following commands in your terminal to get started:

```bash
  1 - git clone https://github.com/otuozeAhmed/real-estate-api
  2 - cd real-estate-api
  # Before the next step, create a file named .env and copy all the content of .env.example to it 
  # (Note: the values here are all examples just to get you up and running, kindly visit mailtrap.io for your personalized dev mail account. This will enable you to receive a bearer token upon account creation.
  # Kindly switch to local console for your email output if you can't set up a maitrap email account)
  # Using this settings in your development.py file: EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
  3 - sudo make build


  ==> visit http://127.0.0.1/api/v1/docs/ to view your project
  4 - sudo make superuser (to create a superuser access to admin)
  admin ==> http://127.0.0.1/admin/
  ext - sudo make logs (to view all container logs)

  # look-up the Makefile in the real-estate-api
  # directory for more handy commands with make
```