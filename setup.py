from setuptools import setup

setup(name='VLAP',
      version='0.1',
      description='Varying Label Amounts Prediction',
      url='https://github.com/gabriben/VLAP',
      author='gabriben',
      author_email='gbndict@gmail.com',
      license='MIT',
      packages=['VLAP'],
      install_requires=[
          'pandas',
          'scikit-learn',
          #'tensorflow',
          #'tensorflow_hub',
          #'tensorflow_addons',
          #'mlflow',
          #'numpy',
          #'transformers'
      ],
      zip_safe=False)
