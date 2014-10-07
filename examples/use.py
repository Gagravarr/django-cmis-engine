#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from examples.models import Folder, Document

# Start Django
import django
django.setup()

# Fetch the doclib folder
doclib = Folder.objects.get(name="documentLibrary")

# Fetch the data lists folder
datalists = Folder.objects.get(name="dataLists")

# Fetch a document in the root of the doclib
info = Document.objects.get(name="example.txt", parent=doclib)
print "The info object contains:"
print "TODO"

# Create a new child folder to hold photos
photos = Folder(name="photos", parent=doclib)
photos.save()

# Upload two photos into it
p1 = Document(name="photo1.jpg", parent=photos)
#TODO add contents
p1.save()

p2 = Document(name="photo2.jpg", parent=photos)
#TODO add contents
p2.save()
