# Automate-updating-catalog-information
 A system that will update the catalog information with data provided.

### Capstone project in Automating with Python by Google

Problem Statement:You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

* Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.
* Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:
* Run a script on your web server to monitor system health.
* Send an email with an alert if the server is ever unhealthy.

The different scripts are:
* changeImage - setting the size and the format of the images provided
* supplier_image_upload - upload the processed images to the web server fruit catalog
* run - add the description provided along with associated data as a JSON dictionary and uploading
* reports - to generate PDF report 
* emails - to generate email
* report_email - process and format the descriptions.
* health_check - for monitoring the resources and to alert.
