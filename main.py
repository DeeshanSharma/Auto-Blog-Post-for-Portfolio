'''
Author: Deeshan Sharma
Date Created: December 7, 2020
Purpose: Purpose of this app is to avoid rewriting the same code again and again and also helpful in saving a lot of time by automating the whole process. In writing blogs for the Blogs page on my portfolio.
'''

import re
import os


def readblog(File='blog.txt'):
    rawblog = ''
    with open(File, 'r') as f:
        rawblog = f.read()
    return rawblog


def process(rawblog):
    filename = re.findall(r'^%fn%(.*?)%fn%$', rawblog, re.MULTILINE)[0]
    title = re.findall(r'^%t%(.*?)%t%$', rawblog, re.MULTILINE)[0]
    header = re.findall(r'^%h%(.*?)%h%', rawblog, re.MULTILINE)[0]
    span = re.findall(r'%s%(.*?)%s%$', rawblog, re.MULTILINE)[0]
    desc = re.findall(r'^%d%(.*?)%d%', rawblog, re.MULTILINE)[0]
    content = rawblog.split('%p%')[1]
    link = re.findall(r'^%l%(.*?)%l%', rawblog, re.MULTILINE)[0]

    header_code = f'''<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="stylesheet" href="/css/style.css" />
		<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
		<script src="https://kit.fontawesome.com/e231f5c914.js" crossorigin="anonymous"></script>
		<title>{title} | Deeshan Sharma</title>
	</head>

	<body>
		<nav class="navigation">
			<div class="nav-brand"><a href="/" class="link"> Deeshan Sharma</a></div>
			<ul class="list nav-links">
				<li class="inline-list-items">
					<a class="link nav-btn" href="/">Home</a>
				</li>
				<li class="inline-list-items">
					<a class="link nav-btn" href="/projects.html">Projects</a>
				</li>
				<li class="inline-list-items">
					<a class="link nav-btn" href="/blogs.html">Blogs</a>
				</li>
			</ul>
		</nav>
		<header class="hero">
			<h1 class="brand-name">{header} <span>{span}</span></h1>
			<p class="desc">{desc}</p>
		</header>
		<section class="section">
			<div class="container purple-section blog">
				<p>{content}</p>
				<br /><br />
				{link}
'''

    footer_code = '''			</div>
		</section>
		<footer>
			<div class="footer">
				<div class="footer-section">
					<div class="footer-heading desc">Site Map:</div>
					<ul class="list">
						<li class="inline-list-items">
							<a class="link" href="/"><i class="fas fa-home"></i> Home</a>
						</li>
						<li class="inline-list-items">
							<a class="link" href="/projects.html"><i class="fas fa-lightbulb"></i> Projects</a>
						</li>
						<li class="inline-list-items">
							<a class="link" href="/blogs.html"><i class="fas fa-book-open"></i> Blogs</a>
						</li>
						<li class="inline-list-items">
							<a class="link" href="/feedback-suggestions.html"><i class="fas fa-comments"></i> Feedback & Suggestions</a>
						</li>
					</ul>
				</div>
				<div class="footer-section">
					<div class="footer-heading desc">Let's Connect Find Me Here:</div>
					<ul class="list social">
						<li class="inline-list-items">
							<a class="link" href="https://www.instagram.com/i_am___unknown__" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>
						</li>
						<li class="inline-list-items">
							<a class="link" href="https://github.com/DeeshanSharma" target="_blank"><i class="fab fa-github"></i> GitHub</a>
						</li>
						<li class="inline-list-items">
							<a class="link" href="https://twitter.com/DeeshanSharma_" target="_blank"><i class="fab fa-twitter"></i> Twitter</a>
						</li>
						<li class="inline-list-items">
							<a class="link" href="https://www.youtube.com/c/TechTeach_ds" target="_blank"><i class="fab fa-youtube"></i> YouTube</a>
						</li>
					</ul>
				</div>
			</div>
			<div class="lower-footer">
				<small>©2020 Deeshan Sharma</small>
				<ul class="list social-icons">
					<li class="inline-list-items">
						<a href="https://www.instagram.com/i_am___unknown__" class="link" target="_blank"><i class="fab fa-instagram"></i></a>
					</li>
					<li class="inline-list-items">
						<a href="https://github.com/DeeshanSharma" class="link" target="_blank"><i class="fab fa-github"></i></a>
					</li>
					<li class="inline-list-items">
						<a href="https://twitter.com/DeeshanSharma_" class="link" target="_blank"><i class="fab fa-twitter"></i></a>
					</li>
				</ul>
			</div>
		</footer>
	</body>
</html>
'''
    blog = f"{header_code}{footer_code}"
    return filename, blog


def writehtml(filename, blog):
    with open(filename, 'w') as w:
        w.write(blog)


def movefile(filename):
    dest = ''
    sysos = os.name
    if 'nt' in sysos.lower():
        dest = f'D:/Code/HTML & CSS/Portfolio/blogs/{filename}'
    else:
        dest = f'/mnt/d/Code/HTML & CSS/Portfolio/blogs/{filename}'
    os.replace(filename, dest)


rawblog = readblog()
filename, blog = process(rawblog)
writehtml(filename, blog)
movefile(filename)
