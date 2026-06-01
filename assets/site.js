// Premium Javascript for responsive UI and client-side logic

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dark Mode Toggle
  const themeToggleBtn = document.getElementById('theme-toggle');
  
  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      themeToggleBtn.innerHTML = `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707.707M12 8a4 4 0 100 8 4 4 0 000-8z"/></svg>`;
    } else {
      document.documentElement.classList.remove('dark');
      themeToggleBtn.innerHTML = `<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>`;
    }
  }

  // Load saved theme
  let savedTheme = localStorage.getItem('currentTheme') || 'light';
  applyTheme(savedTheme);

  themeToggleBtn.addEventListener('click', () => {
    savedTheme = document.documentElement.classList.contains('dark') ? 'light' : 'dark';
    localStorage.setItem('currentTheme', savedTheme);
    applyTheme(savedTheme);
  });

  // 2. Package Manager switcher logic
  const packageManager = localStorage.getItem('packageManager') || 'npm';
  document.body.className = `pm-${packageManager}`;
  
  // Set all tab buttons active matching active package manager
  document.querySelectorAll(`.tab-btn-${packageManager}`).forEach(btn => {
    btn.classList.add('active');
  });

  window.switchPackageManager = function(pm) {
    localStorage.setItem('packageManager', pm);
    document.body.className = `pm-${pm}`;
    
    // De-activate all tabs and active the clicked one on all step codeblocks
    document.querySelectorAll('.code-tab-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    document.querySelectorAll(`.tab-btn-${pm}`).forEach(btn => {
      btn.classList.add('active');
    });
  };

  // 3. Mobile Sidebar Drawer toggle
  const menuToggleBtn = document.getElementById('menu-toggle');
  const sidebarAside = document.querySelector('.sidebar-aside');

  if (menuToggleBtn && sidebarAside) {
    menuToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      sidebarAside.classList.toggle('open');
    });
    
    document.addEventListener('click', (e) => {
      if (!sidebarAside.contains(e.target) && !menuToggleBtn.contains(e.target)) {
        sidebarAside.classList.remove('open');
      }
    });
  }

  // 4. Code Copy Button logic
  window.copyCode = function(btn, index) {
    // Find the code element inside the active block
    // We get the visible code element under the current step
    const parentCodeContainer = btn.closest('.code-container');
    const codeBlock = parentCodeContainer.querySelector('pre');
    
    if (codeBlock) {
      const textToCopy = codeBlock.innerText;
      navigator.clipboard.writeText(textToCopy).then(() => {
        btn.innerHTML = `<svg class="w-4 h-4 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>`;
        setTimeout(() => {
          btn.innerHTML = `<svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"/></svg>`;
        }, 2000);
      });
    }
  };
});
