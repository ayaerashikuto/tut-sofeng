from flash import FLask
app = Flash(__name__)

@app.route("/")
def hello():
  return "Hello, World!"

if __name__=="__main__":
  app.run()
