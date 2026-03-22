const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

const fetch = (...args) =>
    import('node-fetch').then(({ default: fetch }) => fetch(...args));


// Show the form
app.get('/', (req, res) => {
    res.render('index', { error: null, success: null });
});


// Handle form submit → send to Flask
app.post('/submit', async (req, res) => {
    const { name, email, course } = req.body;

    try {
        const response = await fetch(`${BACKEND_URL}/submit`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, course })
        });

        const result = await response.json();

        if (result.success) {
            res.render('index', { error: null, success: 'Data submitted successfully!' });
        } else {
            res.render('index', { error: result.error, success: null });
        }

    } catch (err) {
        res.render('index', { error: 'Could not connect to backend.', success: null });
    }
});


app.listen(3000, () => {
    console.log('Docker mini project running at http://localhost:3000');
});
