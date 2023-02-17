import os

exampleDir = os.path.join(os.environ["SPARK_HOME"], "examples\\jars")
exampleJars = [os.path.join(exampleDir, x) for x in os.listdir(exampleDir)]

print(exampleDir)
print(exampleJars)