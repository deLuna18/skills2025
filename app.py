from flask import Flask, render_template, request, redirect, flash, url_for
import dbhelper 
app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    books = dbhelper.getall_books()
    vets = dbhelper.getall_vets()
    owners = dbhelper.getall_owners()
    pets = dbhelper.getall_pets()
    consultations = dbhelper.getall_consultations()
    return render_template("index.html", books=books, vets=vets, owners=owners, pets=pets, consultations=consultations)

@app.route('/addbook', methods=['POST'])
def add_book():
    isbn = request.form['isbn']
    title = request.form['title']
    author = request.form['author']
    copyright = request.form['copyright']
    edition = request.form['edition']
    price = request.form['price']
    qty = request.form['qty']
    
    ok = dbhelper.add_record(
        'books',
        isbn=isbn,
        title=title,
        author=author,
        copyright=copyright,
        edition=edition,
        price=price,
        qty=qty
    )
    
    message = "New Book Added" if ok else "Error Adding Book"
    flash(message)
    return redirect('/')

@app.route('/findbook', methods=['POST'])
def find_book():
    isbn = request.form['isbn']
    sql = f"SELECT * FROM books WHERE isbn = '{isbn}'"
    book = dbhelper.getprocess(sql)
    
    if book:
        found_book = book[0]  
        message = (f"Book found: ISBN: {found_book['isbn']}, Title: {found_book['title']}, "
                   f"Author: {found_book['author']}, Copyright: {found_book['copyright']}, "
                   f"Edition: {found_book['edition']}, Price: {found_book['price']}, "
                   f"Quantity: {found_book['qty']}")
    else:
        message = "Book not found."
    
    flash(message)  
    return redirect('/')

@app.route('/deletebook', methods=['POST'])
def delete_book():
    isbn = request.form['isbn']
    ok = dbhelper.delete_record('books', isbn=isbn)  
    message = "Book deleted successfully!" if ok else "Error deleting book."  
    flash(message)  
    return redirect('/')

@app.route('/updatebook', methods=['POST']) 
def update_book(): 
    isbn = request.form['isbn']
    title = request.form['title']
    author = request.form['author']
    copyright = request.form['copyright']
    edition = request.form['edition']
    price = request.form['price']
    qty = request.form['qty']
    
    ok = dbhelper.update_record(
        'books',
        isbn=isbn,  
        title=title,
        author=author,
        copyright=copyright,
        edition=edition,
        price=price,
        qty=qty
    )
    
    message = "Book Updated Successfully" if ok else "Error Updating Book"
    flash(message)
    return redirect('/')

@app.route('/addvet', methods=['POST'])
def add_vet():
    vet_id = request.form['vet_id']
    name = request.form['name']
    specialization = request.form['specialization']
    contact = request.form['contact']
    
    ok = dbhelper.add_record(
        'vets',
        vet_id=vet_id,
        name=name,
        specialization=specialization,
        contact=contact
    )
    
    message = "New Vet Added" if ok else "Error Adding Vet"
    flash(message)
    return redirect(url_for('index', module='vets'))

@app.route('/findvet', methods=['POST'])
def find_vet():
    vet_id = request.form['vet_id']
    sql = f"SELECT * FROM vets WHERE vet_id = '{vet_id}'"
    vet = dbhelper.getprocess(sql)
    
    if vet:
        found_vet = vet[0]  
        message = (f"Vet found: ID: {found_vet['vet_id']}, Name: {found_vet['name']}, "
                   f"Specialization: {found_vet['specialization']}, Contact: {found_vet['contact']}")
    else:
        message = "Vet not found."
    
    flash(message)  
    return redirect(url_for('index', module='vets'))

@app.route('/deletevet', methods=['POST'])
def delete_vet():
    vet_id = request.form['vet_id']
    ok = dbhelper.delete_record('vets', vet_id=vet_id)  
    message = "Vet deleted successfully!" if ok else "Error deleting vet."  
    flash(message)  
    return redirect(url_for('index', module='vets'))

@app.route('/updatevet', methods=['POST']) 
def update_vet(): 
    vet_id = request.form['vet_id']
    name = request.form['name']
    specialization = request.form['specialization']
    contact = request.form['contact']
    
    ok = dbhelper.update_record(
        'vets',
        vet_id=vet_id,  
        name=name,
        specialization=specialization,
        contact=contact
    )
    
    message = "Vet Updated Successfully" if ok else "Error Updating Vet"
    flash(message)
    return redirect(url_for('index', module='vets'))

if __name__ == '__main__':
    app.run(debug=True)
