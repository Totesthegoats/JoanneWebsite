# Joanne Colfer - Hypnotherapy & Coaching Website

A modern, responsive website for Joanne Colfer's hypnotherapy and coaching practice in Dublin.

## Features

- **Modern Design**: Clean, calming aesthetic based on hypnotherapy industry best practices
- **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **Single Page Application**: Smooth scrolling between sections for better user experience
- **Professional Layout**: Includes Home, About, Services, Blog, and Contact sections
- **Call-to-Action Buttons**: Strategic placement of booking links throughout the site
- **Mobile Menu**: Hamburger menu for easy navigation on mobile devices
- **Smooth Animations**: Subtle fade-in effects and hover interactions
- **SEO Friendly**: Proper meta tags and semantic HTML structure

## Project Structure

```
JWebsite/
├── index.html          # Main HTML file with all content
├── style.css           # Complete styling and responsive design
├── script.js           # Interactive functionality
└── README.md           # This file
```

## How to Use

### Local Development

1. Simply open `index.html` in your web browser
2. No build process or dependencies required
3. Works offline with all features

### Adding Your Photo

Replace the placeholder in the About section:

1. Add your photo to the project folder (e.g., `joanne-photo.jpg`)
2. In `index.html`, find the `.image-placeholder` div (around line 68)
3. Replace it with:
   ```html
   <img src="joanne-photo.jpg" alt="Joanne Colfer" class="about-photo">
   ```
4. Add this CSS to `style.css`:
   ```css
   .about-photo {
       width: 100%;
       height: 100%;
       object-fit: cover;
       border-radius: var(--radius-md);
       box-shadow: var(--shadow-md);
   }
   ```

## Customization Guide

### Colors

The color scheme is defined in CSS variables at the top of `style.css`:

```css
:root {
    --primary-color: #6B8CAE;        /* Soft blue */
    --primary-dark: #4A6A8A;         /* Darker blue */
    --secondary-color: #B5A6C9;      /* Soft purple */
    --accent-color: #D4A574;         /* Warm gold */
}
```

Change these values to customize the entire color scheme.

### Fonts

Currently using:
- **Headings**: Cormorant Garamond (serif)
- **Body**: Montserrat (sans-serif)

To change fonts, update the Google Fonts link in `index.html` and modify the CSS variables:

```css
--font-heading: 'Your Heading Font', serif;
--font-body: 'Your Body Font', sans-serif;
```

### Content Updates

All content is in `index.html`. Edit the text within each section:
- **Hero**: Lines 33-41
- **About**: Lines 46-91
- **Services**: Lines 97-183
- **Blog**: Lines 190-277
- **Contact**: Lines 285-344

## Deployment Options

### Option 1: Netlify (Recommended - Free)

1. Create a free account at [netlify.com](https://www.netlify.com)
2. Drag and drop your project folder
3. Your site will be live instantly with a free URL
4. Optional: Connect a custom domain

### Option 2: GitHub Pages (Free)

1. Create a GitHub repository
2. Upload your files
3. Go to Settings > Pages
4. Select your main branch
5. Your site will be live at `username.github.io/repository-name`

### Option 3: Traditional Web Hosting

Upload all files via FTP to any web hosting provider.

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Adding More Blog Posts

To add more blog posts, duplicate the `blog-post` article structure in `index.html` and update the content:

```html
<article class="blog-post">
    <div class="blog-content">
        <h3>Your New Blog Title</h3>
        <p class="blog-intro">Your introduction...</p>
        <!-- Add your content -->
    </div>
</article>
```

## Performance

- No external dependencies except Google Fonts
- Optimized images recommended (WebP format preferred)
- Lightweight JavaScript for fast loading
- Mobile-first responsive design

## Contact Information

Current contact details (update in `index.html` if needed):
- **Email**: info@joannecolfer.com
- **Phone**: 085 128 9996
- **Location**: Dublin and Online
- **Instagram**: @joannecolfer
- **Booking**: [Google Calendar Link](https://calendar.app.google/nh6t6apqsXgQ5S2DA)

## Future Enhancements

Consider adding:
- Testimonials section
- Photo gallery
- Additional blog posts
- Newsletter signup
- FAQ section
- Video testimonials
- Online booking system integration

## Support

For technical questions about the website, refer to:
- HTML: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
- CSS: [CSS-Tricks](https://css-tricks.com/)
- JavaScript: [JavaScript.info](https://javascript.info/)

## License

This website is created for Joanne Colfer's exclusive use.

---

**Built with modern web technologies** | Responsive | Fast | Accessible
